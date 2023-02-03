from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class Slide(blocks.StructBlock):
    image = ImageChooserBlock(label=_("Image"))
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    subheading = blocks.CharBlock(max_length=255, required=False, label=_("Subheading"))
    message = blocks.RichTextBlock(
        required=False, features=["bold", "italic", "ul"], label=_("Message")
    )
    link_page = blocks.PageChooserBlock(required=False, label=_("Page"))
    link_url = blocks.URLBlock(required=False, label=_("Url"))
    link_text = blocks.CharBlock(required=False, max_length=255, label=_("Link text"))

    class Meta:
        label = _("Slide")
        label_format = _("Slide")
        icon = "image"


class SlideShowTop(blocks.StructBlock):
    is_visible = blocks.BooleanBlock(default=True, label=_("Visible"))
    slides = blocks.ListBlock((Slide), collapsed=True, label=_("Slides"))

    class Meta:
        template = "home/slideshow.html"
        label = _("Slideshow top")
        label_format = _("Slideshow - top")
        icon = "image"


class SlideShow(blocks.StructBlock):
    is_visible = blocks.BooleanBlock(default=True, label=_("Visible"))
    slides = blocks.ListBlock((Slide), collapsed=True, label=" ")

    class Meta:
        template = "home/slideshow.html"
        label = _("Slideshow")
        icon = "image"


class Card(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, label=_("Heading"))
    subheading = blocks.CharBlock(max_length=255, required=False, label=_("Subheading"))
    content = blocks.RichTextBlock(
        required=False, features=["bold", "italic", "ul"], label=_("Content")
    )
    image = ImageChooserBlock(required=False, label=_("Image"))
    link_page = blocks.PageChooserBlock(required=False, label=_("Page"))
    link_url = blocks.URLBlock(required=False, label=_("Url"))
    link_text = blocks.CharBlock(required=False, max_length=255, label=_("Link text"))

    class Meta:
        template = "home/card.html"
        label = _("Card")
        icon = "form"


class Cards(blocks.StructBlock):
    heading = blocks.CharBlock(
        max_length=255, required=False, default=_("Cards"), label=_("Heading")
    )
    cards = blocks.ListBlock((Card), collapsed=True, label=" ")

    class Meta:
        template = "home/cards.html"
        label = _("Cards")
        icon = "form"


class Cta(Card):
    class Meta:
        template = "home/card.html"
        label = _("Call to action")
        icon = "form"


class Service(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255, label=_("Name"))
    # description = blocks.CharBlock(max_length=255, required=False, label=_("Description"))
    description = blocks.RichTextBlock(
        required=False, features=["bold", "italic", "ul"], label=_("Description")
    )
    image = ImageChooserBlock(required=False, label=_("Image"))
    link_page = blocks.PageChooserBlock(required=False, label=_("Page"))
    link_url = blocks.URLBlock(required=False, label=_("Url"))
    link_text = blocks.CharBlock(required=False, max_length=255, label=_("Link text"))

    class Meta:
        label = _("Service")
        icon = "form"


class Services(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    services = blocks.ListBlock((Service), collapsed=True, label=" ")

    class Meta:
        template = "home/services.html"
        label = _("Services")
        icon = "form"


class Product(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255, label=_("Name"))
    # description = blocks.CharBlock(max_length=255, required=False, label=_("Description"))
    description = blocks.RichTextBlock(
        required=False, features=["bold", "italic", "ul"], label=_("Description")
    )
    price = blocks.DecimalBlock(required=False, decimal_places=2)
    currency_code = blocks.CharBlock(required=False, max_length=3)
    image = ImageChooserBlock(required=False, label=_("Image"))
    link_page = blocks.PageChooserBlock(required=False, label=_("Page"))
    link_url = blocks.URLBlock(required=False, label=_("Url"))
    link_text = blocks.CharBlock(required=False, max_length=255, label=_("Link text"))

    class Meta:
        label = _("Product")
        icon = "form"


class Products(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    products = blocks.ListBlock((Product), collapsed=True, label=" ")

    class Meta:
        template = "home/products.html"
        label = _("Products")
        icon = "form"


class Profile(blocks.StructBlock):
    first_name = blocks.CharBlock(max_length=255, label=_("First name"))
    last_name = blocks.CharBlock(max_length=255, label=_("Last name"))
    image = ImageChooserBlock(required=False, label=_("Image"))
    job = blocks.CharBlock(required=False, max_length=255, label=_("Job"))
    intro = blocks.TextBlock(required=False, max_length=300, blank=True, label=_("Intro"))
    company = blocks.CharBlock(required=False, max_length=255, blank=True, label=_("Company"))
    email = blocks.EmailBlock(required=False, max_length=254, label=_("Email"))
    phone = blocks.CharBlock(required=False, max_length=255, label=_("Phone"))
    instagram = blocks.URLBlock(required=False, help_text="Instagram URL")
    facebook = blocks.URLBlock(required=False, help_text="Facebook URL")
    twitter = blocks.URLBlock(required=False, help_text="Twitter URL")
    youtube = blocks.URLBlock(required=False, help_text="YouTube URL")

    class Meta:
        label_format = _("Profile for") + " " + "{first_name}"
        template = "home/profile.html"
        label = _("Profile")
        icon = "user"


class Testimonial(blocks.StructBlock):
    first_name = blocks.CharBlock(max_length=255, label=_("First name"))
    last_name = blocks.CharBlock(max_length=255, label=_("Last name"))
    subject = blocks.CharBlock(max_length=255, required=False, label=_("Subject"))
    message = blocks.RichTextBlock(max_length=500, required=False, label=_("Message"))
    image = ImageChooserBlock(required=False, label=_("Image"))

    class Meta:
        template = "home/testimonial.html"
        label = _("Testimonial")
        icon = "form"


class Testimonials(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    testimonials = blocks.ListBlock((Testimonial))

    class Meta:
        template = "home/testimonials.html"
        label = _("Testimonials")
        icon = "form"


class Announcement(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, label=_("Heading"))
    subheading = blocks.CharBlock(max_length=255, required=False, label=_("Subheading"))
    message = blocks.RichTextBlock(features=["bold", "italic", "ul"], label=_("Message"))
    image = ImageChooserBlock(required=False, label=_("Image"))
    link_page = blocks.PageChooserBlock(required=False, label=_("Page"))
    link_url = blocks.URLBlock(required=False, label=_("Url"))
    link_text = blocks.CharBlock(required=False, max_length=255, label=_("Link text"))

    class Meta:
        label = _("Announcement")
        icon = "form"


class Announcements(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    announcements = blocks.ListBlock((Announcement), collapsed=True, label=" ")

    class Meta:
        template = "home/announcements.html"
        label = _("Announcements")
        icon = "form"


class RecentBlogPages(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    number_of_pages = blocks.IntegerBlock(
        min_value=1, max_value=10, required=True, default=1, label=_("Number of pages")
    )

    # def number_of_pages(self):
    #     return self.number_of_pages

    class Meta:
        template = "home/recent_blog_pages.html"
        label = _("Recent blog pages")
        icon = "form"
