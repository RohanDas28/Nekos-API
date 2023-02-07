# Generated by Django 4.1.5 on 2023-02-02 05:29

from django.db import migrations
import django_resized.forms
import dynamic_filenames


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0010_alter_image_uploader"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="file",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="",
                force_format="WEBP",
                keep_meta=True,
                quality=100,
                scale=1,
                size=None,
                upload_to=dynamic_filenames.FilePattern(
                    filename_pattern="uploads/images/{uuid:base32}{ext}"
                ),
            ),
            preserve_default=False,
        ),
    ]
