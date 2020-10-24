from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class tags(models.Model):
    nama_kegiatan = models.CharField(max_length=100, null=True)
    deskripsi = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.nama_kegiatan

class peserta(models.Model):
    nama = models.CharField(max_length=50, null=True)
    domisili = models.CharField(max_length=100, null=True)
    kegiatan = models.ManyToManyField(tags)

    def __str__(self):
        return self.nama