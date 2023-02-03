from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from .models import Header


class HeaderAdmin(TranslatableModelAdmin):

    model = Header
    menu_label = _("Header")
    menu_icon = "group"
    menu_order = 1
    add_to_settings_menu = True
    # exclude_from_explorer = False
    # list_display = ["site_name"]
    # inspect_view_enabled = True
    # search_fields = ("email", "last_name", "first_name")


# class FooterAdmin(TranslatableModelAdmin):

#     model = Footer
#     menu_label = _("Footer")
#     menu_icon = "group"
#     menu_order = 2
#     add_to_settings_menu = True
#     # exclude_from_explorer = False
#     # list_display = ["site_name"]
#     # inspect_view_enabled = True
#     # search_fields = ("email", "last_name", "first_name")


# class HeaderFooterAdmin(ModelAdminGroup):
#     menu_label = "Header & Footer"
#     menu_icon = "folder-open-inverse"  # change as required
#     menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
#     # add_to_settings_menu = True
#     items = (HeaderAdmin, FooterAdmin)


modeladmin_register(HeaderAdmin)
# modeladmin_register(FooterAdmin)
# modeladmin_register(HeaderFooterAdmin)
