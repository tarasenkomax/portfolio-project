from django.shortcuts import render
from .models import Job  # Для доступа к базе данных


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
