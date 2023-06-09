# Generated by Django 4.2 on 2023-06-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0005_cardmodel_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardmodel",
            name="category_type",
            field=models.CharField(
                choices=[
                    ("NW", "News"),
                    ("FL", "Folders"),
                    ("BK", "Books"),
                    ("LE", "Lessons"),
                ],
                default="BK",
                max_length=2,
            ),
        ),
        migrations.AddField(
            model_name="cardmodel",
            name="isNews",
            field=models.BooleanField(default=False),
        ),
    ]
