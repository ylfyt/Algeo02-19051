from django.http import request
from django.shortcuts import render
from function.uploadfile import deleteDocuments, conv_txt_to_html
from function.cosinesimilarity import cosinesimilarity
from .models import FileUpload
from .forms import FileUploadForm
import os
# Create your views here.

DIRECTORY = "cosinesimilarity/static/cosinesimilarity/documents/"
# kumpulan document yang diupload
fileName = os.listdir(DIRECTORY)
conv_txt_to_html(fileName)

def home(request):
    formUpload = FileUploadForm()
    context = {
        'form' : formUpload,
    }
    return render(request, "cosinesimilarity/home.html", context)

def uploadFiles(request):
    global fileName
    formUpload = FileUploadForm()
    context = {
        'form' : formUpload,
    }
    if request.method == "POST":
        formUpload = FileUploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('uploadfile')
        if formUpload.is_valid():
            # file baru yang diupload
            newFiles = []
            for file in files:
                if not(str(file) in fileName):
                    newFiles.append(str(file))
                    # upload file
                    instancefile = FileUpload(uploadfile = file)
                    instancefile.save()
            if newFiles != []:
                conv_txt_to_html(newFiles)
                fileName += newFiles
    return render(request, 'cosinesimilarity/home.html', context)

def deleteFiles(request):
    global fileName
    formUpload = FileUploadForm()
    context = {
        'form' : formUpload
    }
    fileName = []
    deleteDocuments()
    return render(request, "cosinesimilarity/home.html", context)

def about(request):
    return render(request, "cosinesimilarity/about.html")

def search(request):
    textQuery = ""
    if (request.method == 'POST'):
        textQuery = request.POST['query']
    contents = cosinesimilarity(textQuery, fileName)

    return render(request, 'cosinesimilarity/search.html', contents)

def dokumen(request):
    count = 0
    post = None
    for key in request.POST.keys():
        if count == 1:
            post = key
        count += 1
    if request.method == "POST":
        return render(request, 'cosinesimilarity/documents/'+post[:-4]+".html")
    return render(request, "cosinesimilarity/home.html")