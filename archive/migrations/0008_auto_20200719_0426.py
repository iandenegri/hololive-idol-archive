# Generated by Django 2.2 on 2020-07-19 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_song_original_artist_jp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='original_artist_jp',
            new_name='romanji_original_artist',
        ),
    ]
