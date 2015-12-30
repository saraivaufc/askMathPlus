from .email import *
from django.utils.translation import ugettext_lazy as _

def send_recover_password():
    subject = _('AskMath - Password Recover')
    sender = 'Arnbjsdradsadsa <saraiva.ufc@gmail.com>'
    recipients = ['Ciano <saraiva.ufc@gmail.com']
    body = '...'
    msg = EmailMessage(subject, body, sender, recipients)
    msg.attach("Une pisdsce jointe.pdf", "%PDF-1.4.%...", mimetype="application/pdf")
    msg.send()
    return HttpResponse("Enviado")
