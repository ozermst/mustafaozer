# Generated by Django 4.1.5 on 2023-02-03 13:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [("wagtailcore", "0078_referenceindex")]

    operations = [
        migrations.CreateModel(
            name="SubscribePage",
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
                ("intro", wagtail.fields.RichTextField(blank=True)),
                ("thank_you_text", wagtail.fields.RichTextField(blank=True)),
                (
                    "button_text",
                    models.CharField(blank=True, max_length=100, verbose_name="Button text"),
                ),
            ],
            options={"verbose_name": "Subscribe page", "verbose_name_plural": "Subscribe page"},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Subscriber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("first_name", models.CharField(max_length=255, verbose_name="First name")),
                ("last_name", models.CharField(max_length=255, verbose_name="Last name")),
                ("email", models.CharField(max_length=254, verbose_name="Email")),
            ],
            options={"verbose_name": "Subscriber", "verbose_name_plural": "Subscribers"},
        ),
    ]
