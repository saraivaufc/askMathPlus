# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMessage


def sender(request, subject, body , to):
    try:
        sender = 'AskMath <askmathplus@gmail.com>'
        msg = EmailMessage(subject, body, sender, to)
        msg.attach("Une pisdsce jointe.pdf", "%PDF-1.4.%...", mimetype="application/pdf")
        msg.send()
        return True
    except Exception, e:
        print e
        return False