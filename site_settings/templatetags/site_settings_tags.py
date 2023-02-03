from django import template
from django.apps import apps
from wagtail.models import Locale

register = template.Library()


@register.simple_tag()
def get_site_name():
    locale = Locale.get_active()
    site_settings = apps.get_model("site_settings", "SiteSetting")
    header = apps.get_model("header", "Header")

    try:
        site_name = header.objects.get(locale_id=locale).site_name

        if site_name:
            return site_name
        else:

            try:
                site_name = site_settings.objects.get.site_name

                if site_name:
                    return site_name
                else:
                    return "Sitename"

            except LookupError:
                pass

    except Exception as e:
        print(e)
        pass


@register.simple_tag()
def get_site_status():
    site_settings = apps.get_model("site_settings", "SiteSettings")

    try:
        site_status = site_settings.objects.get.site_status.status_code

        return site_status

    except Exception as e:
        print(e)
        pass


@register.simple_tag()
def get_site_settings():

    site_setting = apps.get_model("site_settings", "SiteSetting")

    try:
        site_settings = site_setting.objects.all()[0]

        print(site_settings)

        return site_settings

    except Exception as e:
        print(e)
        pass
