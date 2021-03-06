# Generated by Django 2.2.13 on 2020-07-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0015_streamtrack_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamtrack',
            name='timestamp',
            field=models.IntegerField(blank=True, help_text='This is the point in seconds at which this song occurs in a stream.', null=True),
        ),
    ]
