# Generated by Django 4.2.6 on 2023-10-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_policy_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='id_v2',
            field=models.UUIDField(null=True),
        ),
    ]