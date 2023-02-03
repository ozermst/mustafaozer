from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Orderable, TranslatableMixin


class Footer(ClusterableModel):

    panels = [InlinePanel("footer_menu_blocks", label=_("Menu blocks"))]

    def __str__(self):
        return str(_("Footer"))

    class Meta:
        verbose_name = _("Footer")
        verbose_name_plural = _("Footer")


class FooterMenuBlock(ClusterableModel, Orderable):
    parent = ParentalKey("Footer", on_delete=models.CASCADE, related_name="footer_menu_blocks")

    heading = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("heading", heading=_("Heading")),
        FieldPanel("heading_en", heading="Heading"),
        InlinePanel("footer_menu_items", label=_("Menu items")),
    ]

    class Meta:
        ordering = ["sort_order"]
        verbose_name = _("Footer menu block")
        verbose_name_plural = _("Footer menu blocks")


class FooterMenuItem(Orderable):
    parent = ParentalKey(
        "FooterMenuBlock", on_delete=models.CASCADE, related_name="footer_menu_items"
    )

    link_title = models.CharField(max_length=50, blank=True, null=True)
    link_url = models.URLField(max_length=500, blank=True, null=True)
    link_page = models.ForeignKey(
        "wagtailcore.Page", blank=True, null=True, related_name="+", on_delete=models.CASCADE
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)
    submenu_title = models.CharField(
        max_length=50, blank=True, null=True, help_text=_("Submenu title")
    )
    icon = models.ForeignKey(
        "wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    show_when = models.CharField(
        max_length=15,
        choices=[
            ("always", _("Always")),
            ("logged_in", _("When logged in")),
            ("not_logged_in", _("When not logged in")),
        ],
        default="always",
    )

    def show(self, authenticated):
        return (
            (self.show_when == "always")
            or (self.show_when == "logged_in" and authenticated)
            or (self.show_when == "not_logged_in" and not authenticated)
        )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"

    @property
    def submenu_slug(self):
        if self.submenu_title:
            return slugify(self.submenu_title)
        return None

    def __str__(self):
        return self.link_title

    panels = [
        FieldPanel("link_title", heading=_("Link title")),
        FieldPanel("link_title_en", heading="Link title"),
        FieldPanel("link_url", heading=_("Url")),
        FieldPanel("link_page", heading=_("Page")),
        FieldPanel("link_page_en", heading="Link page"),
        FieldPanel("open_in_new_tab", heading=_("Open in new tab")),
        FieldPanel("submenu_title", heading=_("Submenu title")),
        FieldPanel("icon", heading=_("Icon")),
        FieldPanel("show_when", heading=_("Show when")),
    ]

    class Meta:
        ordering = ["sort_order"]
        verbose_name = _("Footer menu item")
        verbose_name_plural = _("Footer menu items")
