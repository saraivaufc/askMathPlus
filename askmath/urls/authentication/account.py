from askmath.views.authentication import ProxyAccount
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

proxy_account = ProxyAccount()

urlpatterns = patterns('',
	 url(r'^$', proxy_account.options),

	 url(r'^options/$', proxy_account.options, name="authentication_options"),
	 url(r'^signin/$', proxy_account.signin, name="authentication_signin"),
	 url(r'^signup/$', proxy_account.signup, name="authentication_signup"),
	 url(r'^logout/$', proxy_account.logout, name="authentication_logout"),
	 url(r'^password/reset/$', 
	 	auth_views.password_reset, 
	 	{
	 		'template_name': 'askmath/authentication/registration/password_reset_form.html',
	 		'post_reset_redirect': '/authentication/password_reset/done/',
	 		'email_template_name': 'askmath/authentication/registration/password_reset_email.html',
	 	},
	 	name='password_reset', 
	 ),

	 url(r'^password_reset/done/$', 
	 	auth_views.password_reset_done, 
	 	{'template_name': 'askmath/authentication/registration/password_reset_done.html',},
	 	name='password_reset_done'),

	 url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 
	 	auth_views.password_reset_confirm,
	 	{'template_name': 'askmath/authentication/registration/password_reset_confirm.html',
	 	'post_reset_redirect': '/authentication/password_reset/complete/',}, 
	 	name='password_reset_confirm'),
	 
	url(r'^password_reset/complete/$', 
	 	auth_views.password_reset_complete,
	 	{'template_name': 'askmath/authentication/registration/password_reset_complete.html',},  
	 	name='password_reset_complete'),
)
