from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Subscriber


class SubscriberAdmin(ModelAdmin):
    """Subscriber admin."""

    model = Subscriber
    menu_label = _("Subscribers")
    menu_icon = "group"
    # menu_order = 150
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "last_name", "first_name")
    search_fields = ("email", "last_name", "first_name")


modeladmin_register(SubscriberAdmin)
