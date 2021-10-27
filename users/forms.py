from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.validators import validate_email
from django import forms
from users.models import User
from .validators import validate_email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form - control py - 4", "placeholder": "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form - control py - 4", "placeholder": "Введите пароль", "max_length": 200}))

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username_passed = cleaned_data.get("username")
        username_req = "ivan"
        if not (username_req in username_passed):
            raise forms.ValidationError("Not a valid username. Try one more time")
        return username_passed

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя пользователя"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите адрес эл. почты"}),
        validators=[validate_email]
    )
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите фамилию"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Подтвердите пароль"}))

    # def clean_email(self):
    #     email_passed = self.cleaned_data.get("email")
    #     email_req = "exampledomain.com"
    #     if not (email_req in email_passed):
    #         raise forms.ValidationError("Not a valid email. Try one more time")
    #     return email_passed

    # def clean(self):
    #     cleaned_data = super(UserRegistrationForm, self).clean()
    #     email_passed = cleaned_data.get("email")
    #     email_req = "exampledomain.com"
    #     if not (email_req in email_passed):
    #         raise forms.ValidationError("Not a valid email. Try one more time")
    #     return email_passed

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')
