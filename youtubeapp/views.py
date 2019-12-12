from django.shortcuts import render, HttpResponse
from .models import Video
from datetime import datetime
import random

# Create your views here.
def index(request):
    kumpulan_video = Video.objects.all()
    kirim = {
        'kumpulan_video' : kumpulan_video,
    }
    return render(request, 'youtubeapp/index.html', kirim)

def show(request, video_id):
    video = Video.objects.get(pk = video_id)
    tambah = video.jumlah_view
    tambah += 1
    video.jumlah_view = tambah
    video.save()

    for konten in Video.objects.all():
        if konten != video:
            random_video = konten
            random_number = random.randint(0,3)
            if random_number == 1:
                break

    kirim = {
        'video' : video,
        'random_video' : random_video
    }
    return render(request, 'youtubeapp/show.html', kirim)

def search(request):
    kata = request.POST['cari']
    hasil_cari = Video.objects.filter(judul__icontains = kata)
    if len(hasil_cari) != 0:
        message = '2'
    else:
        message = '3'

    kirim = {
        'kumpulan_video' : hasil_cari,
        'message' : message
    }
    return render(request, 'youtubeapp/index.html', kirim)

def upload(request):
    return render(request, 'youtubeapp/upload.html', {})

def upload_selesai(request):
    video_baru = Video(
        judul = request.POST['judul'],
        url_video = request.POST['url_video'],
        author = request.POST['author'],
        waktu_upload = datetime.now(),
        foto_author = request.POST['foto_author'],
        deskripsi = request.POST['deskripsi'],
        thumbnail = request.POST['thumbnail'],
        embed = request.POST['embed'],
        jumlah_view = 0
    )
    video_baru.save()
    # return render(request, 'youtubeapp/index.html', {})
    return HttpResponse('Success')

def trending(request):
    trend = Video.objects.all().order_by('-jumlah_view', 'judul')[:4]
    kirim = {
        'kumpulan_video' : trend,
        'message' : '1'
    }
    return render(request, 'youtubeapp/index.html', kirim)