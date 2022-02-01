from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from account.models import Account
from account.root_lib import check_digit
from random import randint
import smtplib


def index_view(request, *args, **kwargs):
    return render(request, 'test3.html')


def signin_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            return HttpResponse('User')
        elif user is not None and user.is_active is False:
            messages.error(request, 'You are not authenticated.')
            return redirect('/home/auth/%s' % username)
        else:
            return HttpResponse('Error')

    return render(request, 'account/signin.html')


def signup_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Password are not matched')
            return redirect('signup')
        elif len(password) < 8:
            messages.error(
                request, 'Password must have more than 8 characters')
            return redirect('signup')
        elif check_digit(password) is False:
            messages.error(request, 'Password must contains numbers')
            return redirect('signup')
        elif Account.objects.filter(email=email):
            messages.error(request, "Email already exist")
            return redirect('signup')
        elif Account.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('signup')

        my_user = Account.objects.create_user(
            email=email, username=username, password=password)
        my_user.is_active = False
        my_user.save()

    return render(request, 'account/signup.html')


def test_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        return redirect('/home/auth/%s' % username)
    return render(request, 'test.html')


def auth_view(request, username, *args, **kwargs):
    if request.method == 'POST':
        otp = request.POST['otp']
        email = Account.objects.get(email=username)
        if otp == email.otp:
            messages.success(request, "Verification successful.")
            email.is_active = True
            email.save()
            return redirect('signin')
        else:
            messages.error(request, "Invalid OTP.")
    return render(request, 'account/auth.html', {'username': username})


def resend_otp(reqest, username, *args, **kwargs):
    otp = randint(1000, 9999)
    email = Account.objects.get(email=username)
    email.otp = otp
    email.save()
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()
    mail.login('python0164@gmail.com', 'superjaw')
    mail.sendmail('fromemail', username, str(otp))
    mail.close()

    return redirect('/home/auth/%s' % username)
    return HttpResponse(f'Hello {username}')


def test2_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse('Welcome')
        messages.error(request, 'Password are not match.')
    return render(request, 'test2.html')
    # def otp_send(request, email_auth, otp_auth):
    #    email = Account.objects.get(email=email_auth)
    #    otp = email.otp
    #    if otp == otp_auth:
    #        messages.success(request, "Verification successful.")
    #        return redirect('signin')
    #    else:
    #        messages.error(request, "Invalid OTP.")
