from django.core.mail import send_mail
from django.db import models
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class ContactMessage(models.Model):

    first_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name=_("First name")
    )
    last_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name=_("Last name")
    )
    email = models.CharField(max_length=254, blank=False, null=False, verbose_name=_("Email"))
    message = models.TextField(max_length=500, blank=False, null=False, verbose_name=_("Message"))

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _("Contact message")
        verbose_name_plural = _("Contact messages")


class ContactPage(Page):
    parent_page_types = ["home.HomePage"]
    max_count = 1

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    button_text = models.CharField(max_length=100, blank=True)

    subject = models.CharField(max_length=100, blank=True)
    from_address = models.EmailField()
    to_address = models.EmailField()

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full", heading=_("Intro")),
        FieldPanel("button_text", heading=_("Button text")),
        FieldPanel("thank_you_text", classname="full", heading=_("Thank you text")),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6", heading=_("From address")),
                        FieldPanel("to_address", classname="col6", heading=_("To address")),
                    ]
                ),
                FieldPanel("subject", heading=_("Subject")),
            ],
            heading=_("Email settings"),
        ),
    ]

    def serve(self, request):
        from contact.forms import ContactForm

        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save()

                if self.to_address:

                    from_address = self.from_address
                    recipient_list = []
                    recipient_list.append(self.to_address)
                    subject = self.subject + " - " + form.cleaned_data["email"]
                    message = form.cleaned_data["message"]

                    send_mail(subject, message, from_address, recipient_list)

                return render(
                    request, "contact/contact_page_landing.html", {"page": self, "contact": contact}
                )

                # return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()

        return render(request, "contact/contact_page.html", {"page": self, "form": form})

    class Meta:
        verbose_name = _("Contact page")
        verbose_name_plural = _("Contact pages")
