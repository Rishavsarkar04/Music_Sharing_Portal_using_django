# Generated by Django 4.2.2 on 2023-06-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_musicfiles_singer_alter_musicfiles_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicfiles',
            name='image',
            field=models.ImageField(null=True, upload_to='song_images'),
        ),
    ]
