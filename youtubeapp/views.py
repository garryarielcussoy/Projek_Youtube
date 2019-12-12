from django.shortcuts import render, HttpResponse
from .models import Video
from datetime import datetime

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
    kirim = {
        'video' : video
    }
    return render(request, 'youtubeapp/show.html', kirim)

def search(request):
    kata = request.POST['cari']
    hasil_cari = Video.objects.filter(judul__icontains = kata)
    kirim = {
        'kumpulan_video' : hasil_cari
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