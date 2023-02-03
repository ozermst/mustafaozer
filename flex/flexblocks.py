from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ShortText(blocks.StructBlock):
    text = blocks.CharBlock(required=False, max_length=255)

    class Meta:
        template = "flex/short_text.html"
        label = _("Short text")
        icon = "form"


class LongText(blocks.StructBlock):
    text = blocks.TextBlock(required=False, max_length=500)

    class Meta:
        template = "flex/long_text.html"
        label = _("Long text")
        icon = "form"


class RichText(blocks.StructBlock):
    # heading = blocks.CharBlock(required=False, max_length=255)
    text = blocks.RichTextBlock(required=False)

    class Meta:
        template = "flex/richtext.html"
        label = _("RichText")
        icon = "form"
