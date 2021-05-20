from django.contrib import admin
from .models import Project, Image, Tag, DetailBody

admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(DetailBody)