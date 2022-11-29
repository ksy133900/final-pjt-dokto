from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "age",
            "genre",
            "day",
            "time",
            "password1",
            "password2",
        ]
        labels = {
            "age": "나이",
            "genre": "선호하는 장르",
            "day": "선호하는 요일",
            "time": "선호하는 시간",
        }

    # OperationalError at /accounts/signup/
    # no such column: accounts_user.nickname
    def signup(self, request, user):
        # form에 기입된 데이터를 가져오기 위해 cleaned_data 사용
        user.age = self.cleaned_data["age"]
        user.genre = self.cleaned_data["genre"]
        user.day = self.cleaned_data["day"]
        user.time = self.cleaned_data["time"]

        user.save()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile()
        fields = ["intro", "image", "nickname"]
        labels = {
            "image": "프로필 사진",
            "intro": "소개글",
            "nickname": "닉네임",
        }
