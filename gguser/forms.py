from django import forms
from .models import User
from django.contrib.auth.hashers import check_password, make_password


class IndexForm(forms.Form):
    userName = forms.CharField(max_length=64)

    def clean(self):
        cleaned_data = super().clean()
        userName = cleaned_data.get('userName')
        print(userName)

class LoginForm(forms.Form):
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

        if userid and password:
            try:
                user = User.objects.get(userid=userid)
            except User.DoesNotExist:
                self.add_error('userid', '등록된 아이디가 없습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')


class RegisterForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=64, label='아이디'
    )
    username = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=64, label='이름'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        # No problem then, 
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 다릅니다.')
                self.add_error('re_password', '비밀번호가 다릅니다.')
        # I need to add check reduplication code.
        
        try:
            user = User.objects.get(userid=userid)
            self.add_error('password', '비밀번호가 다릅니다.')
        except User.DoesNotExist:
            self.add_error('userid', '등록된 아이디가 없습니다.')
            