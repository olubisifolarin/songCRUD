from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from musicapp.serializer import *

# Create your views here.

class ArtisteView(APIView):
    def get(self, request):
        if request.method =='GET':
            artiste = Artiste.objects.all()
            artiste = ArtisteSerializer(artiste, many=True)
            return Response(artiste.data)
    
def update_artiste(request, artiste_id):
    artiste = Artiste.objects.get(id=artiste_id)
    artiste_serializer = ArtisteSerializer(instance=artiste, data=request.data)
    if artiste_serializer.is_valid():
        artiste_serializer.save()
        return Response(artiste_serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

def delete_artiste(request, artiste_id):
    if request.method == 'DELETE':
        artiste = Artiste.objects.get(id=artiste_id)
        artiste.delete()
        return Response("Artiste deleted successfully")
        
        
class SongView(APIView):
    def get(self, request):
        if request.method == 'GET':
            song = Song.objects.all()
            song_serializer = SongSerializer(song, many=True)
            return Response(song_serializer.data)
        
        elif request.method == 'POST':
            song_serializer = SongSerializer(data=request.data)
            if song_serializer.is_valid():
                song_serializer.save
                return Response(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
def update_song(request, song_id):
    song = Song.objects.get(id=song_id)
    song_serializer = SongSerializer(instance=song, data=request.data)
    if song_serializer.is_valid():
        song_serializer.save()
        return Response(song_serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
def delete_song(request, song_id):
    if request.method == 'DELETE':
        song = Song.objects.get(id=song_id)
        song.delete()
        return Response("Song deleted successfully")
    
class LyricsView(APIView):
    def get(self, request):
        if request.method  == 'GET':
            lyrics = Lyrics.objects.all()
            lyrics_serializer = LyricsSerializer(lyrics, many=True)
            return Response(lyrics_serializer.data)
        

            
    