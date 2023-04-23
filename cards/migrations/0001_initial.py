# Generated by Django 4.2 on 2023-04-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CardModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
                ("imglink", models.CharField(max_length=200)),
                ("file", models.FileField(upload_to="uploads/")),
            ],
        ),
    ]
