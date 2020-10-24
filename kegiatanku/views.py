from .forms import tambahOrang, tambahTag
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    orang = peserta.objects.all()
    return render(request, 'kegiatanku/index.html', {'orang':orang})

def tambahAstaga(request):
    form = tambahOrang()

    if request.method == 'POST':
        form = tambahOrang(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form}
    return render(request, 'kegiatanku/form.html', context)

def tambahKegiatan(request):
    form = tambahTag()

    if request.method == 'POST':
        form = tambahTag(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {'form':form}
    return render(request, 'kegiatanku/kegiatan.html', context)

    