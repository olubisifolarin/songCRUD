from django.contrib import admin
from musicapp.models import Lyrics, Song, Artiste


admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyrics)
