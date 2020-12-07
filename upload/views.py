from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFile
from .forms import Upload


# Create your views here.
def upload(request):
    if request.method == 'POST':
        fm = UploadFile(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'successfully uploaded notes')
            return redirect("allnotes")
    else:
        fm = UploadFile()

    return render(request, 'upload.html', {'upload': fm})


def allnotes(request):
    dis = Upload.objects.all()
    return render(request, 'allnotes.html', {'notes': dis})


def update(request, id):
    if request.method == 'POST':
        pi = Upload.objects.get(pk=id)
        fm = UploadFile(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'successfully updated notes')
    else:
        pi = Upload.objects.get(pk=id)
        fm = UploadFile(instance=pi)
    return render(request, 'update.html', {'fm': fm})


def delete(request, id):
    pi = Upload.objects.get(pk=id)
    pi.delete()
    messages.success(request,'successfully deleted')
    return redirect("allnotes")

