from allauth.account.forms import SignupForm, LoginForm


class SignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })

    def save(self, request):
        user = super(SignUpForm, self).save(request)
        return user


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'})



