from django.shortcuts import render
from .models import Video

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