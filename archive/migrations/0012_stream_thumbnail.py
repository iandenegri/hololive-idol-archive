# Generated by Django 2.2.13 on 2020-07-27 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0011_auto_20200721_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='thumbnail',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
