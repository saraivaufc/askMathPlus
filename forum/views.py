"""
All forum logic is kept here - displaying lists of forums, threads 
and posts, adding new threads, and adding replies.
"""

from datetime import datetime

from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, Context, loader
from django.template.defaultfilters import striptags, wordwrap
from django.utils.translation import ugettext as _
#from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView


from forum.models import Forum, Thread, Post
from forum.forms import CreateThreadForm, ReplyForm, EditPost

FORUM_PAGINATION = getattr(settings, 'FORUM_PAGINATION', 10)
LOGIN_URL = getattr(settings, 'LOGIN_URL', '/accounts/login/')

def forums_list(request):
    """
    Forum frontpage, displays a list of forums.
    """
    queryset = Forum.objects.for_groups(request.user.groups.all()).filter(parent__isnull=True)
    
    return ListView.as_view( request,
                        queryset=queryset)

def forum(request, slug):
    """
    Displays a list of threads within a forum.
    Threads are sorted by their sticky flag, followed by their 
    most recent post.
    """
    qs = Forum.objects.for_groups(request.user.groups.all()).select_related()
    f = get_object_or_404(qs, slug=slug)

    form = CreateThreadForm(forum=f)
    child_forums = f.child.for_groups(request.user.groups.all())
    
    return ListView.as_view( request,
                        queryset=f.thread_set.select_related().all(),
                        paginate_by=FORUM_PAGINATION,
                        template_object_name='thread',
                        template_name='forum/thread_list.html',
                        extra_context = {
                            'forum': f,
                            'child_forums': child_forums,
                            'form': form,
                        })

def thread(request, thread):
    """
    Increments the viewed count on a thread then displays the 
    posts for that thread, in chronological order.
    """
    try:
        t = Thread.objects.select_related().get(pk=thread)
        if not Forum.objects.has_access(t.forum, request.user.groups.all()):
            raise Http404
    except Thread.DoesNotExist:
        raise Http404
    
    p = t.post_set.select_related('author').all().order_by('time')

    t.views += 1
    t.save()

    form = ReplyForm()

    page = request.GET.get('page', 1)
    if page == 'all':
        paginate_by = None
    else:
        paginate_by = FORUM_PAGINATION

    return ListView.as_view( request,
                        queryset=p,
                        paginate_by=paginate_by,
                        template_object_name='post',
                        template_name='forum/thread.html',
                        extra_context = {
                            'forum': t.forum,
                            'thread': t,
                            'form': form,
                        })


@login_required
def reply(request, thread, extra_context=None):
    """
    If a thread isn't closed, and the user is logged in, post a reply
    to a thread. Note we don't have "nested" replies at this stage.
    """
    t = get_object_or_404(Thread, pk=thread)
    if t.closed:
        return HttpResponseServerError()
    if not Forum.objects.has_access(t.forum, request.user.groups.all()):
        return HttpResponseForbidden()

    preview = False
    p = None

    if request.method == "POST":
        form = ReplyForm(request.POST)
        preview = request.POST.get('preview')
        p = Post(
            thread=t, 
            author=request.user,
            time=datetime.now(),
            )
        if form.is_valid():
            p.body = form.cleaned_data['body']
            
            if not preview:
                p.save()

            if not preview:
                return HttpResponseRedirect(p.get_absolute_url())
    else:
        form = ReplyForm()
    
    return render_to_response('forum/reply.html',
        RequestContext(request, {
            'form': form,
            'forum': t.forum,
            'post': p,
            'preview': preview,
            'thread': t,
        }))


@login_required
def newthread(request, forum, extra_context=None):
    """
    Rudimentary post function - this should probably use 
    newforms, although not sure how that goes when we're updating 
    two models.

    Only allows a user to post if they're logged in.
    """
    f = get_object_or_404(Forum, slug=forum)
    
    if not Forum.objects.has_access(f, request.user.groups.all()):
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = CreateThreadForm(forum=f, data=request.POST)
        if form.is_valid():
            t = Thread(
                forum=f,
                title=form.cleaned_data['title'],
            )
            t.save()

            p = Post(
                thread=t,
                author=request.user,
                body=form.cleaned_data['body'],
                time=datetime.now(),
            )
            p.save()
    
            return HttpResponseRedirect(t.get_absolute_url())
    else:
        form = CreateThreadForm(forum=f)

    ctx = extra_context or {}
    ctx.update({'form': form,
        'forum': f,
        })

    return render_to_response('forum/newthread.html',
        ctx, RequestContext(request))

       
@login_required
def delete_post(request, id, thread, extra_context=None, template_name=None):
    """
    Deletes a post, if the user is the author.
    """
    post = get_object_or_404(Post, id=id, thread__id=thread)
    
    if not request.user == post.author:
        raise Http404
    
    if request.method == 'POST' and request.POST.get('confirm'):
        post.delete()
        request.user.message_set.create(message=_('Deleted post'))
        return HttpResponseRedirect(post.thread.get_absolute_url())

    ctx = extra_context or {}
    ctx['post'] = post

    return render_to_response(template_name or 'forum/post_delete.html',
            RequestContext(request, ctx))


@login_required
def edit_post(request, id, thread=None, form_class=None, 
        template_name=None, extra_context=None):
    """
    edit existing post view
    """

    post = get_object_or_404(Post, id=id, thread__id=thread)
    form_class = form_class or EditPost

    if not request.user == post.author:
        raise Http404

    preview = False

    if request.method == 'POST':
        preview = request.POST.get('preview', False)
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=not preview)
            if not preview:
                return HttpResponseRedirect(post.thread.get_absolute_url())
    else:
        form = form_class(instance=post)
    

    ctx = extra_context or {}
    ctx.update({'form': form,
        'post': post,
        'preview': preview,
        })

    return render_to_response(template_name or 'forum/post_edit.html',
        ctx, RequestContext(request))
