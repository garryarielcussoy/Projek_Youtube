# Generated by Django 3.0 on 2019-12-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0003_auto_20191212_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='deskripsi',
            field=models.TextField(default=''),
        ),
    ]
