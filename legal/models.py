from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class LegalIndexPage(Page):

    parent_page_types = ["home.HomePage"]
    subpage_types = ["flex.FlexPage", "legal.LegalPage"]
    max_count = 1

    def get_context(self, request):
        context = super().get_context(request)
        legal_pages = self.get_children().live().order_by("-first_published_at")
        context["legal_pages"] = legal_pages
        return context

    class Meta:
        verbose_name = _("Legal index page")
        verbose_name_plural = _("Legal index page")


class LegalPage(Page):

    intro = models.TextField(max_length=500)
    body = RichTextField()

    title_widget = forms.TextInput(
        attrs={"placeholder": _("Enter document title"), "help_text": ""}
    )

    content_panels = [
        FieldPanel("intro", heading=_("Intro")),
        FieldPanel("body", widget=title_widget, classname="title", heading=_("Body")),
    ]

    class Meta:
        verbose_name = _("Legal page")
        verbose_name_plural = _("Legal page")
