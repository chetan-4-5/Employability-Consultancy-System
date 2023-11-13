from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class JobSearchForm(forms.Form):
    search_query = forms.CharField(max_length=255)
