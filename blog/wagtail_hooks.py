from taggit.models import Tag
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from .models import BlogPage, BlogTag

# class TagsModelAdmin(ModelAdmin):
# class TagsModelAdmin(TranslatableModelAdmin):
#     BlogTag.panels = [FieldPanel("name"), FieldPanel("slug")]  # only show the name field
#     model = BlogTag
#     menu_label = "Tags"
#     menu_icon = "tag"  # change as required
#     menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
#     list_display = ["name", "slug"]
#     search_fields = ("name",)


# modeladmin_register(TagsModelAdmin)
