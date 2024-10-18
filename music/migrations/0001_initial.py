# Generated by Django 5.1 on 2024-08-21 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=50, verbose_name='Artist Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Artist created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest artist update')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=50, verbose_name='Album Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Album created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest album update')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist', verbose_name='Artist Album')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songThumbnail', models.ImageField(help_text='.jpg, .png, .jpeg, .gif, .svg supported', upload_to='thumbnail/', verbose_name='Song Thumbnail')),
                ('song', models.FileField(help_text='.mp3 supported only', upload_to='songs/', verbose_name='Song')),
                ('songName', models.CharField(max_length=50, verbose_name='Song Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Song created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest song update')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album', verbose_name='Song Album')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
    ]
