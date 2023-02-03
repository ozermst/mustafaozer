from captcha.fields import ReCaptchaField
from django import forms

from subscribe.models import Subscriber


class SubscribeForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Subscriber
        fields = ["first_name", "last_name", "email"]
