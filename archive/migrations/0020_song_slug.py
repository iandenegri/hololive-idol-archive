# Generated by Django 2.2.13 on 2020-07-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0019_idol_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default='owo!'),
            preserve_default=False,
        ),
    ]
