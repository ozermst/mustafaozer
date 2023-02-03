from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from .models import SiteStatus, SiteTheme


class SiteStatusAdmin(TranslatableModelAdmin):

    model = SiteStatus
    menu_label = _("Status")
    menu_icon = "site"
    # menu_order = 900
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ["status", "title"]
    # search_fields = "title"


class SiteThemeAdmin(ModelAdmin):

    model = SiteTheme
    menu_label = _("Themes")
    menu_icon = "site"
    # menu_order = 850
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ["theme"]


class SiteSettingsAdmin(ModelAdminGroup):
    menu_label = "Site settings"
    menu_icon = "folder-open-inverse"  # change as required
    # menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
    # add_to_settings_menu = True
    items = (SiteStatusAdmin, SiteThemeAdmin)


modeladmin_register(SiteStatusAdmin)
modeladmin_register(SiteThemeAdmin)
# modeladmin_register(SiteSettingsAdmin)
