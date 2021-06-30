from django.conf import settings
import threading
from django.core.mail import send_mail

class SendThredEmail(threading.Thread):
    def __init__(self, sendTo, msg):
        self.sendTo = sendTo
        self.msg = msg
        print("Emailing...")
        threading.Thread.__init__(self)

    def run(self):
        email = SendEmail(self.sendTo, self.msg)
        email.fireEmail()

class SendEmail:
    def __init__(self, sendTo, msg):
        self.email_from = settings.EMAIL_HOST_USER
        self.sendTo = sendTo
        self.msg = msg

    def fireEmail(self):
        subject = 'Vaccine seat availability Notification Touchmedia Ads'
        recipient_list = [self.sendTo,]
        send_mail(subject, self.msg, self.email_from, recipient_list)
