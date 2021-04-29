from django import forms
from django.contrib.auth.hashers import check_password, make_password


class SummonerForm(forms.Form):
    userid = forms.CharField(error_messages={
        'required': '아이디를 입력해주세요.'
    }, max_length=64, label="아이디")
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력해주세요.'
    }, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        # No problem then,
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')
