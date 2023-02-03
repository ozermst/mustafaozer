from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class RichText(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, max_length=255)
    richtext = blocks.RichTextBlock(required=False)

    class Meta:
        template = "about/richtext.html"
        label = _("RichText")
        icon = "form"


class Profile(blocks.StructBlock):
    first_name = blocks.CharBlock(max_length=255, label=_("First name"))
    last_name = blocks.CharBlock(max_length=255, label=_("Last name"))
    job = blocks.CharBlock(required=False, max_length=255, label=_("Job"))
    image = ImageChooserBlock(required=False, label=_("Image"))
    intro = blocks.TextBlock(required=False, max_length=500, blank=True, label=_("Intro"))
    company = blocks.CharBlock(required=False, max_length=255, blank=True, label=_("Company"))
    email = blocks.EmailBlock(required=False, max_length=254, label=_("Email"))
    phone = blocks.CharBlock(required=False, max_length=255, label=_("Phone"))
    instagram = blocks.URLBlock(required=False, label="Instagram", help_text="Instagram URL")
    facebook = blocks.URLBlock(required=False, label="Facebook", help_text="Facebook URL")
    twitter = blocks.URLBlock(required=False, label="Twitter", help_text="Twitter URL")
    youtube = blocks.URLBlock(required=False, label="YouTube", help_text="YouTube URL")

    class Meta:
        label_format = "{first_name}"
        template = "about/profile.html"
        label = _("Profile")
        icon = "user"


class Address(blocks.StructBlock):
    address_line_1 = blocks.CharBlock(max_length=255, label=_("Address line 1"))
    address_line_2 = blocks.CharBlock(required=False, max_length=255, label=_("Address line 2"))
    postal_code = blocks.CharBlock(required=False, max_length=255, label=_("Postal code"))
    district = blocks.CharBlock(required=False, max_length=255, label=_("District"))
    city = blocks.CharBlock(max_length=255, label=_("City"))
    state = blocks.CharBlock(required=False, max_length=255, label=_("State"))
    country = blocks.CharBlock(max_length=255, label=_("Country"))

    class Meta:
        template = "about/address.html"
        label = _("Address")
        icon = "user"


class Employment(blocks.StructBlock):
    date_from = blocks.DateBlock(label=_("Start date"))
    date_to = blocks.DateBlock(label=_("End date"))
    employer = blocks.CharBlock(max_length=255, label=_("Employer"))
    job = blocks.CharBlock(max_length=255, label=_("Job"))
    city = blocks.CharBlock(max_length=255, label=_("City"))
    country = blocks.CharBlock(max_length=255, label=_("Country"))

    class Meta:
        label_format = "{employer}"
        label = _("Employment")
        icon = "form"


class EmploymentHistory(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, required=False, label=_("Heading"))
    employment_history = blocks.ListBlock(
        (Employment), collapsed=True, label=_("Employment history")
    )

    class Meta:
        template = "about/employment_history.html"
        label = _("Employment history")
        icon = "form"


class University(blocks.StructBlock):
    date_from = blocks.DateBlock(label=_("Start date"))
    date_to = blocks.DateBlock(label=_("End date"))
    degree = blocks.CharBlock(max_length=255, label=_("Degree"))
    university = blocks.CharBlock(max_length=255, label=_("University"))
    faculty = blocks.CharBlock(max_length=255, label=_("Faculty"))
    department = blocks.CharBlock(max_length=255, label=_("Department"))
    city = blocks.CharBlock(max_length=255, label=_("City"))
    country = blocks.CharBlock(max_length=255, label=_("Country"))

    class Meta:
        label = _("University")
        icon = "form"


class UniversityEducation(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255, label=_("Heading"))
    university_education = blocks.ListBlock(
        (University), collapsed=True, label=_("University education")
    )

    class Meta:
        template = "about/university_education.html"
        label = _("University education")
        icon = "form"
