from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from .models import Footer


class FooterAdmin(ModelAdmin):

    model = Footer
    menu_label = _("Footer")
    menu_icon = "group"
    menu_order = 2
    add_to_settings_menu = True


modeladmin_register(FooterAdmin)
