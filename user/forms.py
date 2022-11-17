from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm


class SignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })
        self.fields['username'].label = "Логин"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Повтор пароля"
        self.fields['email'].label = "Почта"

    def save(self, request):
        user = super(SignUpForm, self).save(request)
        return user


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'input'})
        self.fields['password'].widget.attrs.update({
            'class': 'input'})
        self.fields['login'].label = "Логин"
        self.fields['password'].label = "Пароль"
        self.fields['remember'].label = "Запомнить меня"


class PasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'input'})


