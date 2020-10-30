from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre =models.CharField(max_length=100)
    album_logo_link=models.CharField(max_length=1000)
    is_favorite_album = models.BooleanField(default=False)
    #is_favorite1 = models.BooleanField(default=False)
    def __str__ (self):
        return self.album_title+'-'+self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title= models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__ (self):
        return self.song_title 

class favourite(models.Model):
    #more fields
    fav = models.ManyToManyField(Album, related_name='favAlbum')