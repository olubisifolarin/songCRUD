from django.contrib import admin
from musicapp.models import Lyrics, Song, Artiste

# Register your models here.
admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyrics)