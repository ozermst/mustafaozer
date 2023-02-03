from django.apps import apps
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.core.models import Page
from wagtail.fields import StreamField

from . import flexblocks


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    max_count = 1

    flexcomponents = StreamField(
        [
            ("slideshow_top", flexblocks.SlideShowTop()),
            ("profile", flexblocks.Profile()),
            ("cta", flexblocks.Cta()),
            # ("slideshow", flexblocks.SlideShow()),
            ("services", flexblocks.Services()),
            ("products", flexblocks.Products()),
            ("announcements", flexblocks.Announcements()),
            ("recent_blog_pages", flexblocks.RecentBlogPages()),
            ("testimonials", flexblocks.Testimonials()),
        ],
        block_counts={
            "slideshow_top": {"max_num": 1},
            "profile": {"max_num": 1},
            "cta": {"max_num": 1},
            # "slideshow": {"max_num": 1},
            "services": {"max_num": 1},
            "products": {"max_num": 1},
            "announcements": {"max_num": 1},
            "recent_blog_pages": {"max_num": 1},
            "testimonials": {"max_num": 1},
        },
        use_json_field=True,
        blank=True,
        collapsed=True,
    )

    def get_context(context, request):
        context = super().get_context(request)
        # number_of_pages = self.RecentBlogPages.number_of_pages
        try:
            recent_blog_pages = (
                apps.get_model("blog", "BlogPage")
                .objects.live()
                .order_by("-first_published_at")[:10]
                # .order_by("-first_published_at")[:number_of_pages]
            )

            # context["recent_blog_pages"] = recent_blog_pages

            return context

        except Exception as e:
            print(e)
            pass

    content_panels = Page.content_panels + [FieldPanel("flexcomponents", heading=_("Components"))]

    class Meta:
        verbose_name = _("Homepage")
        verbose_name_plural = _("Homepage")
