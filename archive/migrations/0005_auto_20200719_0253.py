# Generated by Django 2.2 on 2020-07-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_idol_jp_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='channel',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='idol',
            name='channel_id',
            field=models.CharField(blank=True, max_length=264, unique=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='link',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=264, unique=True),
        ),
    ]
