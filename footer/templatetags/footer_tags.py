from django import template
from django.apps import apps
from wagtail.models import Locale

register = template.Library()


@register.simple_tag()
def get_footer_menu(page, logged_in):

    menu_blocks = []

    # locale = Locale.get_active().language_code
    footer = apps.get_model("footer", "Footer")

    try:
        footer_menu_blocks = footer.objects.first().footer_menu_blocks.all()

        for block in footer_menu_blocks:

            menu_block = {}
            menu_block["heading"] = block.heading

            candidates = block.footer_menu_items.all()

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

                menu_block["menu_items"] = menu_items

            menu_blocks.append(menu_block)

        return menu_blocks

    except Exception as e:
        print(e)
        pass
