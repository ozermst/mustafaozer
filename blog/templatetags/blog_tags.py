from django import template
from django.apps import apps
from wagtail.models import Locale

register = template.Library()


@register.simple_tag()
def get_recent_blog_pages():

    locale = Locale.get_active()
    blog_page = apps.get_model("blog", "BlogPage")

    try:

        recent_blog_pages = (
            blog_page.objects.live().filter(locale=locale).order_by("-first_published_at")[:10]
        )

        return recent_blog_pages

    except Exception as e:
        print(e)
        pass
