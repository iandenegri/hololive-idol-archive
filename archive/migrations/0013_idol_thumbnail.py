# Generated by Django 2.2.13 on 2020-07-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0012_stream_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='idol',
            name='thumbnail',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
