from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from . import models
from django import forms
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.conf import settings
from .models import profanity_filter

def isNum(data):
    if data:
        data = str(data)
        try:    
            int(data)
            return True
        except ValueError:
            return False
    return True

class ResetPassword(forms.Form):
    new_password1 = forms.CharField(
        label= "New password:",
        error_messages = {
            'required': ("Oops, you forgot to enter your password!"),
        },
        widget=forms.PasswordInput(attrs={
            'class':'form-control py-2 my-2',
        }),
    )
    new_password2 = forms.CharField(
        label= "Confirm new password:",
        error_messages = {
            'required': ("Oops, you forgot to confirm your password!"),
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control py-2 my-2',
        }),
    )
    
    def clean(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            password_validation.validate_password(password1)
            if password1 != password2:
                raise forms.ValidationError("Passwords need to match 🙂")
        return self.cleaned_data 
     
    
class GenerateEmail(PasswordResetForm):
    email = forms.EmailField(
        label= "Email:",
       error_messages = {
            'required': ("Oops, you forgot about your e-mail!"),
        },
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class':'form-control py-2 my-2'
        })
    )
    
    def clean(self):
        email = self.cleaned_data.get('email')
        if email and not get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError({'email': ["We couldn't find account with such email 🙁"]})
        return self.cleaned_data

class JoinForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control py-2 my-1',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control py-2 my-1'
                }
            ),
        }
        error_messages = {
            'email': {
                'required': ("Oops, you forgot to enter your email!"),
                'invalid': ("Ey, that's not a valid email address!")
            },
            'first_name': {
                'required': ("Let us know what to call you!"),
            },
            'password1': {
                'required': ("Oops, you forgot to enter your password!"),
                'invalid': ("Ey, that's not a valid email address!"),
            },     
            'password1': {
                'required': ("Oops, you forgot to enter password confirmation!"),
                'invalid': ("Ey, that's not a valid email address!")
            },    
             
        }
    accepts_tos = forms.CharField(required=True, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input'
        },
    ))
        
    def __init__(self, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control py-2'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control py-2'})
        self.fields['password1'].error_messages = {
            'required': ("Oops, you forgot to enter your password!"),
        }
        self.fields['password2'].error_messages = {
            'required': ("Oops, you forgot to confirm your password!"),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError({'email': ["Account with this email already exists"]})
        
        return cleaned_data
    
    
class LoginForm(forms.ModelForm):    
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control py-2 my-1'
                },
            ),
            'password':forms.PasswordInput(
                attrs={
                    'class':'form-control py-2 my-1'
                }
            ),
        }
        error_messages = {
            'email': {
                'required': ("Oops, you forgot to enter your email!"),
                'invalid': ("Ey, that's not a valid email address!")
            },
            'password': {
                'required': ("Oops, you forgot to enter your password!"),
            },
        }
        
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user or not user.is_active:
                raise forms.ValidationError("Wrong credentials")
        return self.cleaned_data    
    
    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user
        
    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')

    #     if email is not None and password:
    #         self.user_cache = authenticate(self.request, email=email, password=password)
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #     return self.cleaned_data
        
class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['isd_code'].required = True
        self.fields['first_name'].required = True
                    
    class Meta:
        model = models.User
        fields = (
            'first_name',
            'isd_code',
            'phone_number',
            'display_phone',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            # in the future i will crate a choice field in which instead of typing you will just choose the isd code from a list (in the future tho)
            'isd_code': forms.TextInput(
                attrs={
                    'class':'form-control isd'
                },
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class':'form-control phone'
                },
            ),
            'display_phone': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                },
            ),          
        }
        error_messages = {
            'first_name': {
                'required': ("Your name can't be empty!"),
            },
        }
        
    def clean(self):
        isd = self.cleaned_data.get('isd_code')
        phone = self.cleaned_data.get('phone_number')
        name = self.cleaned_data.get('first_name')
        display_phone = self.cleaned_data.get('display_phone')
        if not isNum(phone) or not isNum(isd) and isd:
            raise forms.ValidationError("Please enter correct values")
        if name:
            profanity_filter(name)
        if display_phone and not phone:
            raise forms.ValidationError('What is your phone number?')
        return self.cleaned_data
    
        
class SendEmail(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        data = super().clean()

        name = data.get('name').strip()
        sender = data.get('email')
        subject = data.get('inquiry')

        msg = f'{name} with email {sender} said:'
        msg += f'\n"{subject}"\n\n'
        msg += data.get('message')

        return subject, msg

    def send(self):
        subject, msg = self.get_info()
        send_mail(
            subject=subject,
            message=msg,
            sender=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER]
        )