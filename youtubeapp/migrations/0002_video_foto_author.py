# Generated by Django 3.0 on 2019-12-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='foto_author',
            field=models.CharField(default='', max_length=200),
        ),
    ]
