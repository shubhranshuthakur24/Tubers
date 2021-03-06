from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    youtubers = Youtuber.objects.order_by(
        '-created_date')
    featured_youtubers = Youtuber.objects.order_by(
        '-created_date').filter(is_featured=True)
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'youtubers': youtubers,
    }
    return render(request, 'webpages/home.html', data)


def aboutUs(request):
    return render(request, 'webpages/aboutUs.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
