from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from . import flexblocks


class FlexIndexPage(Page):
    class Meta:
        abstract = True


class FlexPage(Page):

    parent_page_types = ["legal.LegalIndexPage"]
    subpage_types = []
    max_count = 5

    flexcomponents = StreamField(
        [
            ("short_text", flexblocks.ShortText()),
            ("long_text", flexblocks.LongText()),
            ("richtext", flexblocks.RichText()),
        ],
        block_counts={
            "short_text": {"max_num": 5},
            "long_text": {"max_num": 5},
            "richtext": {"max_num": 5},
        },
        use_json_field=True,
        collapsed=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [FieldPanel("flexcomponents", heading=_("Components"))],
            heading=_("Flexible components"),
        )
    ]

    class Meta:
        verbose_name = _("Flex page")
        verbose_name_plural = _("Flex page")
