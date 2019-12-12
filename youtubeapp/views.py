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
    unique_key = video.url_video[32:]
    kirim = {
        'video' : video,
        'unik' : unique_key
    }
    return render(request, 'youtubeapp/show.html', kirim)