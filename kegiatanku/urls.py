from django.urls import path
from . import views

app_name = 'kegiatanku'

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah/', views.tambahAstaga, name='tambah'),
    path('tambahKegiatan/', views.tambahKegiatan, name='tambahKegiatan')
]