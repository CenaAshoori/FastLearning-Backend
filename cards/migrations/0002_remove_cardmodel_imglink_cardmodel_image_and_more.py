# Generated by Django 4.2 on 2023-04-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cardmodel",
            name="imglink",
        ),
        migrations.AddField(
            model_name="cardmodel",
            name="image",
            field=models.FileField(
                default="uploads/image.png", upload_to="uploads/images/"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cardmodel",
            name="file",
            field=models.FileField(upload_to="uploads/files/"),
        ),
    ]
