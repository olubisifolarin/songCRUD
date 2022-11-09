from django.urls import path
from musicapp import views

app_name = 'musicapp'

urlpatterns = [
    path('', views.SongView.as_view(), name='song'),
    path('update/<int:song_id>', views.update_song, name='update-song'),
    path('delete/<int:song_id>', views.delete_song, name='delete-song'),
    path('artiste/', views.ArtisteView.as_view(), name='artiste'),
    path('update/<int:artiste_id>', views.update_artiste, name='update-artiste'),
    path('delete/<int:artiste_id>', views.delete_artiste, name='delete-ariste'),
    path('lyrics/', views.LyricsView.as_view(), name='lyrics'),
    
    
    
  
]