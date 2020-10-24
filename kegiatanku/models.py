from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class peserta(models.Model):
    nama = models.CharField(max_length=50, null=True)
    domisili = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nama

class tags(models.Model):
    peserta_kegiatan = models.ForeignKey(peserta, null=True, on_delete=models.SET_NULL)
    nama_kegiatan = models.CharField(max_length=100, null=True)
    deskripsi = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.nama_kegiatan