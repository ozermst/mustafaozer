from captcha.fields import ReCaptchaField
from django import forms

from contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactMessage
        fields = ["first_name", "last_name", "email", "message"]
