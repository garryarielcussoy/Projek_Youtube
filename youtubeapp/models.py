from django.db import models

# Create your models here.
class Video(models.Model):
    judul = models.CharField(max_length=200, default='')
    url_video = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    waktu_upload = models.DateTimeField('Waktu Upload')
    foto_author = models.CharField(max_length=200, default='')
    deskripsi = models.TextField(default='')

    def __str__(self):
        return self.judul

class URLUnik(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    unik = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.video_id