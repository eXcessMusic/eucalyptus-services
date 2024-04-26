# Generated by Django 5.0.4 on 2024-04-26 14:27

import django.db.models.deletion
import event.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_remove_artist_events_remove_artist_song_song_artist'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artist.artist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='artwork',
            field=models.ImageField(upload_to=event.models.event_artwork_directory_path),
        ),
    ]
