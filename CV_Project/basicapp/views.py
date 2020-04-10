from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from basicapp.models import skills_languages, skills_frameworks, skills_tools_vcs

class index(TemplateView):
    template_name='basicapp/Index.html'
