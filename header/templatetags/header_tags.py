from django import template
from django.apps import apps
from wagtail.models import Locale

register = template.Library()


@register.simple_tag()
def get_header_menu(page, logged_in):

    locale = Locale.get_active()
    header = apps.get_model("header", "Header")

    try:

        candidates = header.objects.get(locale_id=locale).header_menu_items.all()

        menu_items = []

        for candidate in candidates:
            if candidate.show_when == "always":
                if candidate.link_page:
                    if candidate.link_page.live and candidate.link_page.show_in_menus:
                        menu_items.append(
                            {
                                "title": candidate.title,
                                "url": candidate.link,
                                "icon": candidate.icon,
                            }
                        )

                elif candidate.link_url and candidate.title:
                    menu_items.append(
                        {
                            "title": candidate.title,
                            "url": candidate.link_url,
                            "icon": candidate.icon,
                        }
                    )

            if candidate.show_when == "logged_in" and logged_in:

                if candidate.link_page:
                    if candidate.link_page.live and candidate.link_page.show_in_menus:
                        menu_items.append(
                            {
                                "title": candidate.title,
                                "url": candidate.link,
                                "icon": candidate.icon,
                            }
                        )

                elif candidate.link_url and candidate.title:
                    menu_items.append(
                        {
                            "title": candidate.title,
                            "url": candidate.link_url,
                            "icon": candidate.icon,
                        }
                    )

            if candidate.show_when == "not_logged_in" and not logged_in:

                if candidate.link_page:
                    if candidate.link_page.live and candidate.link_page.show_in_menus:
                        menu_items.append(
                            {
                                "title": candidate.title,
                                "url": candidate.link,
                                "icon": candidate.icon,
                            }
                        )

                elif candidate.link_url and candidate.title:
                    menu_items.append(
                        {
                            "title": candidate.title,
                            "url": candidate.link_url,
                            "icon": candidate.icon,
                        }
                    )

        return menu_items

    except Exception as e:
        print(e)
        pass
