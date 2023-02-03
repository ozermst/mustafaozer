from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

# from .models import Menu


# class MenuAdmin(TranslatableModelAdmin):

#     model = Menu
#     menu_label = _("Menus")
#     menu_icon = "group"
#     # menu_order = 140
#     add_to_settings_menu = True
#     exclude_from_explorer = False
#     list_display = ["title"]
#     # search_fields = ("email", "last_name", "first_name")


# modeladmin_register(MenuAdmin)
