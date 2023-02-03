import uuid

from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _


class SignupForm(SignupForm):

    username = forms.CharField(
        max_length=100, widget=forms.HiddenInput(), label=_("Username"), initial=uuid.uuid4
    )

    first_name = forms.CharField(
        max_length=100,
        label=_("First name"),
        widget=forms.TextInput(attrs={"placeholder": _("First name")}),
    )
    last_name = forms.CharField(
        max_length=100,
        label=_("Last name"),
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )
