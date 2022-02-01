from django.contrib import messages
from django.shortcuts import redirect, render
from account.models import Account
import smtplib
from random import randint


def check_digit(string_, *args, **kwargs):
    return any(char.isdigit() for char in string_)


def resend_otp(request, email):
    otp = randint(1000, 9999)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()
    mail.login('python0164@gmail.com', 'superjaw')
    mail.sendmail('fromemail', email, str(otp))
    mail.close()

    return redirect('/home/auth/%s' % email)
