# Generated by Django 2.2.13 on 2020-07-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0016_auto_20200729_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stream',
            name='slug',
            field=models.SlugField(default='owo'),
            preserve_default=False,
        ),
    ]