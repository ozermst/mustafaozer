from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, BaseSiteSetting, register_setting
from wagtail.models import Orderable, TranslatableMixin


@register_setting
class SiteSetting(BaseSiteSetting):
    site_name = models.CharField(max_length=255, blank=True)
    site_status = models.ForeignKey(
        "SiteStatus", blank=True, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    theme = models.ForeignKey(
        "SiteTheme", blank=True, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    branding_logo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    instagram = models.URLField(blank=True, help_text="Instagram URL")
    facebook = models.URLField(blank=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, help_text="YouTube Channel URL")

    panels = [
        FieldPanel("site_name", heading=_("Site name")),
        FieldPanel("branding_logo", heading=_("Branding logo")),
        FieldPanel("site_status", heading=_("Site status")),
        FieldPanel("theme", heading=_("Theme")),
        MultiFieldPanel(
            [FieldPanel("email"), FieldPanel("phone")], heading=_("Contact information")
        ),
        MultiFieldPanel(
            [
                FieldPanel("instagram"),
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("youtube"),
            ],
            heading=_("Social media settings"),
        ),
    ]

    class Meta:
        verbose_name = _("Site settings")
        verbose_name_plural = _("Site settings")
        # unique_together = ("translation_key", "locale")


class SiteStatus(TranslatableMixin):
    ACTIVE = "ACT"
    CONSTRUCTION = "CON"
    COMING_SOON = "COS"
    MAINTENANCE = "MNT"
    STATUS_CHOICES = [
        (ACTIVE, _("Active")),
        (COMING_SOON, _("Coming soon")),
        (MAINTENANCE, _("Under maintenance")),
        (CONSTRUCTION, _("Under construction")),
    ]

    def __str__(self):
        for choice in self.STATUS_CHOICES:
            if choice[0] == self.status:
                return str(choice[1])

    @property
    def status_code(self):
        for choice in self.STATUS_CHOICES:
            if choice[0] == self.status:
                return str(choice[0])

    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    countdown_timer = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    panels = [
        FieldPanel("status", heading=_("Site status")),
        FieldPanel("countdown_timer", heading=_("Countdown timer")),
        FieldPanel("title", heading=_("Title")),
        FieldPanel("image", heading=_("Image")),
    ]

    class Meta:
        verbose_name = _("Site status")
        verbose_name_plural = _("Site statuses")
        unique_together = (("translation_key", "locale"), ("locale", "status"))


class SiteTheme(models.Model):

    LIGHT = "light"
    DARK = "dark"
    CUPCAKE = "cupcake"

    THEME_CHOICES = [(LIGHT, _("Light")), (DARK, _("Dark")), (CUPCAKE, _("Cupcake"))]

    theme = models.CharField(max_length=10, choices=THEME_CHOICES)
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    def __str__(self):
        for theme in self.THEME_CHOICES:
            if theme[0] == self.theme:
                return str(theme[1])

    @property
    def theme_code(self):
        for theme in self.THEME_CHOICES:
            if theme[0] == self.theme:
                return str(theme[0])

    panels = [FieldPanel("theme", heading=_("Site theme")), FieldPanel("image", heading=_("Image"))]

    class Meta:
        verbose_name = _("Site theme")
        verbose_name_plural = _("Site themes")
