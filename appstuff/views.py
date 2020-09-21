from django.shortcuts import render
from .models import * 


def show_files(request):
    data=File.objects.all()
    return render(request, "index.html", {'files': data})
