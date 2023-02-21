from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from ia import settings
from . import models, forms
from django.contrib.auth.decorators import login_required
import shortuuid
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from datetime import date, datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from smtplib import SMTPDataError
import post
from django.contrib import messages


# def reset_password_generate(request):
#     form = forms.ResetPassword(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         email = form['email'].value()
#         user = models.User.objects.get(email=email)

#         token = default_token_generator.make_token(user)
#         print(token)
        
#         message='''
#         django.test1@outlook.com

#         Here is Your link to reset Your password:
        
#         {}
        
#         '''
#         # send_mail('Rest Your password', message, 'django.test1@outlook.com', form['email'].value())
#         return redirect(reverse('email-sent'))
#     return render(request, 'send_email.html', {'form': form})

def reset_generate_link(request):
    form = forms.GenerateEmail(request.POST or None)
    if request.method == 'POST' and form.is_valid():   
        try:     
            form.save(
                subject_template_name='password/password_reset_subject.txt',
                email_template_name='password/password_reset_email.html',
                from_email='django.test1@outlook.com',
                html_email_template_name=None,
                extra_email_context=None,
                request=request
            )
            return redirect(reverse('email-sent'))
        except SMTPDataError:
            raise Http404
    return render(request, 'password/send_email.html', {'form': form})
    
def reset_email_sent(request):
    return render(request, 'password/email_sent.html')

def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist, ValidationError):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        form = forms.ResetPassword(request.POST or None, use_required_attribute=False)
        if request.method == 'POST' and form.is_valid():
            user.set_password(str(form.cleaned_data['new_password1']))
            user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, "Password has been updated.")
            return redirect(reverse('home'))
        return render(request, 'password/reset_password.html', {'form': form})
    return redirect(reverse('home'))

def signup_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    form = forms.JoinForm(request.POST or None, use_required_attribute=False)
    if request.method == 'POST' and form.is_valid():
        account = form.save(commit=False)
        account.id = post.views.idExists(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))
        account.save()
        login(request, account)
        return redirect(reverse('join-message'))
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    form = forms.LoginForm(request.POST or None, use_required_attribute=False)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(reverse('home'))
    return render(request, 'login.html', {'form': form})

@login_required()
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def account_view(request, user_id):
    user = get_user_model().objects.filter(id=user_id).first()
    if not user:
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        else:
            raise Http404
            
    posts = post.models.Post.objects.filter(author=user)
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'account.html', {'context': context})

@login_required()
def edit_account(request):
    if request.POST:
        form = forms.EditUserForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.isd_code = form.cleaned_data['isd_code']
            request.user.phone_number = form.cleaned_data['phone_number']
            request.user.display_phone = form.cleaned_data['display_phone']
            request.user.save(update_fields=['first_name', 'isd_code', 'phone_number', 'display_phone'])
            messages.add_message(request, messages.INFO, 'Your personal information have been updated.')
            return redirect(reverse('account-view', kwargs={'user_id': request.user.id}))
    else:
        form = forms.EditUserForm(initial={'first_name': request.user.first_name, 'isd_code': request.user.isd_code, 'phone_number': request.user.phone_number, 'display_phone': request.user.display_phone})
    return render(request, 'edit_account.html', {'form': form})

@login_required()
def join_message(request):
    name = request.user.first_name
    return render(request, 'join_message.html', {'name': name})

def tos(request):
    return render(request, 'tos.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

@login_required()
def delete_account(request):
    request.user.delete()
    messages.add_message(request, messages.INFO, 'Account has been deleted successfully.')
    return redirect(reverse('home'))