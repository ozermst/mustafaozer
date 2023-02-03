from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import ItemBase, TagBase
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Locale, Orderable, Page, TranslatableMixin
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail_localize.fields import SynchronizedField


def limit_category_choices():
    locale = Locale.get_active()
    # limit = models.Q(locale_id="1")
    limit = models.Q(locale_id=locale)
    return limit


class BlogIndexPage(Page):

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.BlogPage"]
    max_count = 1

    def get_context(self, request):
        context = super().get_context(request)
        blog_pages = self.get_children().live().order_by("-first_published_at")
        context["blog_pages"] = blog_pages
        return context

    class Meta:
        verbose_name = _("Blog index page")
        verbose_name_plural = _("Blog index page")


@register_snippet
class BlogTag(TranslatableMixin, TagBase):
    free_tagging = False

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", max_length=100, allow_unicode=True, editable=False)

    class Meta:
        verbose_name = _("Blog tag")
        verbose_name_plural = _("Blog tags")
        unique_together = (("translation_key", "locale"), ("locale", "slug"), ("locale", "name"))


class TaggedBlog(TranslatableMixin, ItemBase):
    tag = models.ForeignKey(BlogTag, related_name="tagged_blogs", on_delete=models.CASCADE)
    content_object = ParentalKey(
        to="blog.BlogPage", on_delete=models.CASCADE, related_name="tagged_items"
    )

    class Meta:
        unique_together = ("translation_key", "locale")


class BlogPage(Page):
    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []

    date = models.DateTimeField(verbose_name=("Post date"))
    intro = models.TextField(max_length=500)
    body = RichTextField()
    tags = ClusterTaggableManager(through="blog.TaggedBlog", blank=True)
    author = models.ForeignKey("blog.BlogAuthor", blank=True, null=True, on_delete=models.SET_NULL)

    def main_image(self):
        gallery_item = self.images_gallery.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [index.SearchField("intro"), index.SearchField("body")]

    title_widget = forms.TextInput(
        attrs={"placeholder": _("Enter blog page title"), "help_text": ""}
    )

    content_panels = [
        FieldPanel("title", widget=title_widget, classname="title", heading=_("Title")),
        MultiFieldPanel(
            [
                FieldPanel("date", heading=_("Post date")),
                FieldPanel("author", heading=_("Blog author")),
                FieldPanel("tags", heading=_("Tags")),
                InlinePanel("categories", label="category"),
            ],
            heading=_("Meta data"),
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel("intro", heading=_("Intro")),
                FieldPanel("body", heading=_("Body")),
                InlinePanel("images_gallery", min_num=1, label=_("Images gallery")),
            ],
            heading=_("Content"),
            classname="collapsed",
        ),
    ]

    class Meta:
        verbose_name = _("Blog page")
        verbose_name_plural = _("Blog pages")


class BlogPageImagesGallery(TranslatableMixin, Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="images_gallery")
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(blank=False, max_length=255)

    override_translatable_fields = [SynchronizedField("image", overridable=False)]

    panels = [FieldPanel("image", heading=_("Image")), FieldPanel("caption", heading=_("Caption"))]

    class Meta:
        verbose_name = _("Blog page images gallery")
        verbose_name_plural = _("Blog page images gallery")
        unique_together = ("translation_key", "locale")


class BlogTagFilterPage(Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]

    def get_context(self, request):

        tag = request.GET.get("tag")
        blog_pages = BlogPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context["blog_pages"] = blog_pages
        return context

    class Meta:
        verbose_name = _("Blog tag filter page")
        verbose_name_plural = _("Blog tag filter page")


class BlogCategoryFilterPage(Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]

    def get_context(self, request):
        category = request.GET.get("category")
        blog_pages = BlogPage.objects.filter(categories__blog_category__name=category)

        context = super().get_context(request)
        context["blog_pages"] = blog_pages
        return context

    class Meta:
        verbose_name = _("Blog category filter page")
        verbose_name_plural = _("Blog category filter page")


class BlogPageBlogCategory(TranslatableMixin):
    page = ParentalKey("blog.BlogPage", on_delete=models.CASCADE, related_name="categories")
    blog_category = models.ForeignKey(
        "blog.BlogCategory", on_delete=models.CASCADE, related_name="+"
    )

    def __str__(self):
        return self.blog_category.name

    panels = [FieldPanel("blog_category")]

    class Meta:
        unique_together = (("translation_key", "locale"), ("page", "blog_category"))


@register_snippet
class BlogCategory(TranslatableMixin):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    def __str__(self):
        return self.name

    override_translatable_fields = [SynchronizedField("icon", overridable=False)]

    panels = [FieldPanel("name", heading=_("Name")), FieldPanel("icon", heading=_("Icon"))]

    class Meta:
        verbose_name = _("Blog category")
        verbose_name_plural = _("Blog categories")
        unique_together = ("translation_key", "locale")


@register_snippet
class BlogAuthor(TranslatableMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    instagram = models.URLField(blank=True, help_text="Instagram URL")
    facebook = models.URLField(blank=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, help_text="YouTube Channel URL")

    def __str__(self):
        return self.first_name + " " + self.last_name

    override_translatable_fields = [
        SynchronizedField("first_name", overridable=False),
        SynchronizedField("last_name", overridable=False),
        SynchronizedField("image", overridable=False),
        SynchronizedField("email", overridable=False),
        SynchronizedField("phone", overridable=False),
        SynchronizedField("website", overridable=False),
        SynchronizedField("instagram", overridable=False),
        SynchronizedField("facebook", overridable=False),
        SynchronizedField("twitter", overridable=False),
        SynchronizedField("youtube", overridable=False),
    ]

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("first_name", heading=_("First name")),
                FieldPanel("last_name", heading=_("Last name")),
                FieldPanel("job", heading=_("Job")),
                FieldPanel("image", heading=_("Image")),
            ],
            heading=_("Profile"),
        ),
        MultiFieldPanel(
            [FieldPanel("email", heading=_("Email")), FieldPanel("phone", heading=_("Phone"))],
            heading=_("Contact information"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("instagram"),
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("youtube"),
            ],
            heading=_("Social media information"),
        ),
    ]

    class Meta:
        verbose_name = _("Blog author")
        verbose_name_plural = _("Blog authors")
        unique_together = ("translation_key", "locale")
