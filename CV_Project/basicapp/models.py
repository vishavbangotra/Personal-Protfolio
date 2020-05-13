from django.db import models

# class skills_languages(models.Model):
#     name = models.CharField(max_length=126)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     def __str__(self):
#         return self.name
#
# class skills_frameworks(models.Model):
#     name = models.CharField(max_length=126)
#
#     def __str__(self):
#         return self.name
#
# class skills_tools_vcs(models.Model):
#     name = models.CharField(max_length=126)
#
#     def __str__(self):
#         return self.name

class project(models.Model):
    title = models.CharField(max_length=128, default=True)
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=256)
    github = models.URLField()
