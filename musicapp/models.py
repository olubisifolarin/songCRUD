from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    
class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500)
    artisteId = models.IntegerField() 
    date_released = models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField()
   
     
    def __str__(self):
        return self.title
    
class Lyrics(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    songId = models.IntegerField() 
    content = models.TextField()
    
    
    def __str__(self):
        return self.content