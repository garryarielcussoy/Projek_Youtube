from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request):
    kumpulan_video = Video.objects.all()
    kirim = {
        'kumpulan_video' : kumpulan_video
    }
    return render(request, 'youtubeapp/index.html', kirim)