# Generated by Django 3.0 on 2019-12-12 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0004_video_deskripsi'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLUnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unik', models.CharField(default='', max_length=255)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeapp.Video')),
            ],
        ),
    ]
