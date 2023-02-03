from django import template
from django.apps import apps
from wagtail.models import Locale

register = template.Library()


@register.simple_tag()
def get_header_menu(page, logged_in):

    locale = Locale.get_active()
    header = apps.get_model("header_footer", "Header")

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


@register.simple_tag()
def get_footer_menu(page, logged_in):

    try:
        locale = Locale.get_active()
        footer = apps.get_model("header_footer", "Footer")

        footer_menu_blocks = footer.objects.get(locale_id=locale).footer_menu_blocks.all()

        menu_items = []
        menu_block = {}
        menu_blocks = []

        for footer_menu_block in footer_menu_blocks:

            menu_block["header"] = footer_menu_block.header

            candidates = footer_menu_block.footer_menu_items.all()

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

                menu_block["menu_items"] = menu_items

                menu_blocks.append(menu_block)

        return menu_blocks

    except footer.DoesNotExist:
        pass


""" 
@register.simple_tag()
def get_menu(slug, page, logged_in):
    try:
        locale = Locale.get_active()
        candidates = Menu.objects.get(slug=slug, locale_id=locale).menu_items.all()

        menu_items = []

        for candidate in candidates:
            if (
                candidate.show(logged_in)
                and candidate.link_page.live
                and candidate.link_page.show_in_menus
            ):
                menu_items.append(
                    {
                        "title": candidate.title,
                        # "url": candidate.trans_url(language_code),
                        "url": candidate.link,
                        "slug": candidate.submenu_slug,
                        # "page": candidate.trans_page(language_code),
                        "page": candidate.link_page,
                        "icon": candidate.icon,
                    }
                )
        return menu_items
    except Menu.DoesNotExist:
        pass
 """
