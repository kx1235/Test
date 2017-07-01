from django.contrib import admin
from .models import Album

#adding albums to admin page
admin.site.register(Album)

