from django.db import migrations


def forwards_func(apps, schema_editor):
    WagtailSite = apps.get_model("wagtailcore.Site")
    Page = apps.get_model("wagtailcore.Page")

    try:
        root_page = Page.objects.get(id=3)
    except Page.DoesNotExist:
        root_page = Page.objects.get(slug="anasayfa")

    wagtail_site, created = WagtailSite.objects.get_or_create(
        hostname="localhost", root_page=root_page, is_default_site=True
    )

    if not created:
        wagtail_site.hostname = "localhost"
        wagtail_site.root_page = root_page
        wagtail_site.is_default_site = True
        wagtail_site.save()

    try:
        Page.objects.filter(id=2).delete()
    except Exception as e:
        print(e)
        pass


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("home", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
