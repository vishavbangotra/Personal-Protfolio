from django.shortcuts import render
# from django.views.generic import View, TemplateView, ListView
from basicapp.models import project

def index(request):
    projects = project.objects.all()

    return render(request, 'basicapp/index.html', {'projects': projects})
