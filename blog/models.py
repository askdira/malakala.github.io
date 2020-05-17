from django.db import models

# Create your models here.
class Projek(models.Model):
    judul = models.CharField(max_length=100)
    desk = models.TextField()
    teknik = models.CharField(max_length=20)
    gambar = models.FilePathField(path="/img")