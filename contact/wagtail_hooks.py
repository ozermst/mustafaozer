from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ContactMessage


class ContactMessageAdmin(ModelAdmin):

    model = ContactMessage
    menu_label = _("Contact messages")
    menu_icon = "group"
    # menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "last_name", "first_name", "message")
    search_fields = ("email", "last_name", "first_name")


modeladmin_register(ContactMessageAdmin)
