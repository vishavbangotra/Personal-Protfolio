from django.contrib import admin
from .models import skills_frameworks, skills_tools_vcs, skills_languages

admin.site.register(skills_languages)
admin.site.register(skills_frameworks)
admin.site.register(skills_tools_vcs)
