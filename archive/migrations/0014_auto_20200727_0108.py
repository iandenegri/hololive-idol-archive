# Generated by Django 2.2.13 on 2020-07-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0013_idol_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
    ]
