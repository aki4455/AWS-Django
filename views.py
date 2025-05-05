

from django.shortcuts import render, get_object_or_404, redirect
from .models import Countries
from django.urls import reverse
from .forms import AlbumForm
from django.views.generic import (
  CreateView,
  DetailView,
  DeleteView,
  ListView,
  UpdateView,
  ListView,
)

# Create your views here.
def album_list(request):
    queryset = Countries.objects.all()
    context = {
        'album_list': queryset
    }
    return render(request, 'album_list.html', context)

def album_detail(request, country):
    obj = get_object_or_404(Countries, country=country)  # Fixed the country=country
    context = {
        'object': obj
    }
    return render(request, 'album_detail.html', context)


def album_create(request):
    form = AlbumForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('al-list')  # Or your redirect view
    return render(request, 'album_create.html', {'form': form}) 


def album_delete(request, country):
  obj = get_object_or_404(Countries, country=country)
  if request.method == "POST":
    obj.delete()
    return redirect("al-list")
  context = {
    "object":obj
  }
  return render(request, "album_delete.html", context)

  

  




  