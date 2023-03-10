# Generated by Django 4.1.5 on 2023-02-03 13:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [("wagtailcore", "0078_referenceindex")]

    operations = [
        migrations.CreateModel(
            name="LegalIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                )
            ],
            options={"verbose_name": "Legal index page", "verbose_name_plural": "Legal index page"},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LegalPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", models.TextField(max_length=500)),
                ("body", wagtail.fields.RichTextField()),
            ],
            options={"verbose_name": "Legal page", "verbose_name_plural": "Legal page"},
            bases=("wagtailcore.page",),
        ),
    ]
