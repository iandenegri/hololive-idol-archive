# Generated by Django 2.2 on 2020-07-22 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0010_stream_original_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.RemoveField(
            model_name='song',
            name='playlist_number',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='songs',
        ),
        migrations.AddField(
            model_name='stream',
            name='songs',
            field=models.ManyToManyField(blank=True, through='archive.StreamTrack', to='archive.Song'),
        ),
        migrations.AddField(
            model_name='streamtrack',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Song'),
        ),
        migrations.AddField(
            model_name='streamtrack',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Stream'),
        ),
    ]