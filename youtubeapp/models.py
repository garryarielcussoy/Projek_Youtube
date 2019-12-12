from django.db import models

# Create your models here.
class Video(models.Model):
    judul = models.CharField(max_length=200, default='')
    url_video = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    waktu_upload = models.DateTimeField('Waktu Upload')
    foto_author = models.CharField(max_length=200, default='')
    deskripsi = models.TextField(default='')
    thumbnail = models.CharField(max_length=200, default='')
    embed = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.judul