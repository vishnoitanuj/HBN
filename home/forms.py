from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout
from .models import Innovation


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if username and password:
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm,self).clean()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username(choose an easy one!!)')
    first_name= forms.CharField(label='First name ')
    last_name = forms.CharField(label='Last name ')
    phone = forms.IntegerField(label='Contact Number ')
    email = forms.EmailField(label='Email address',)
    email2=forms.EmailField(label='Confirm Email ')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone',
            'email',
            'email2',
            'password',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email!=email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

    # def clean_phone(self):
    #     phone = self.changed_data('phone')
    #     phone_qs = User.objects.filter(phone=phone)
    #     if phone_qs.exists():
    #         raise forms.ValidationError("This number has already been registered")
    #     return phone

class FeedbackForm(forms.Form):
    feedback = forms.CharField(max_length=600)

class InnovationForm(forms.ModelForm):
    class Meta:
        model=Innovation
        fields = [
            'innovator',
            'title',
            'location',
            'image',
            'detail',
            'file',
        ]