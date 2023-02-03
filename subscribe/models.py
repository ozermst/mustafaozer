from django.db import models
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class Subscriber(models.Model):

    first_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name=_("First name")
    )
    last_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name=_("Last name")
    )
    email = models.CharField(max_length=254, blank=False, null=False, verbose_name=_("Email"))

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")


class SubscribePage(Page):
    parent_page_types = ["home.HomePage"]
    max_count = 1

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    button_text = models.CharField(max_length=100, blank=True, verbose_name="Button text")

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full", heading=_("Intro")),
        FieldPanel("button_text", heading=_("Button text")),
        FieldPanel("thank_you_text", classname="full", heading=_("Thank you text")),
    ]

    def serve(self, request):
        from subscribe.forms import SubscribeForm

        if request.method == "POST":
            form = SubscribeForm(request.POST)
            if form.is_valid():
                subscriber = form.save()
                return render(
                    request,
                    "subscribe/subscribe_page_landing.html",
                    {"page": self, "subscriber": subscriber},
                )
        else:
            form = SubscribeForm()

        return render(request, "subscribe/subscribe_page.html", {"page": self, "form": form})

    class Meta:
        verbose_name = _("Subscribe page")
        verbose_name_plural = _("Subscribe page")
