from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from . import flexblocks


class AboutPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1

    flexcomponents = StreamField(
        [
            ("profile", flexblocks.Profile()),
            ("employment_history", flexblocks.EmploymentHistory()),
            ("university_education", flexblocks.UniversityEducation()),
            ("richtext", flexblocks.RichText()),
        ],
        block_counts={
            "profile": {"max_num": 1},
            "employment_history": {"max_num": 1},
            "university_education": {"max_num": 1},
            "richtext": {"max_num": 1},
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
        verbose_name = _("About page")
        verbose_name_plural = _("About page")
