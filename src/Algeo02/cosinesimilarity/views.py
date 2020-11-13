from django.http import request
from django.shortcuts import render
from function.stemming import stemmingDokumen, stemmingQuery
from function.uploadfile import cosine_similarity, deleteDocuments
from function.cosinesimilarity import cosinesimilarity
from .models import FileUpload
from .forms import FileUploadForm
import os
# Create your views here.

# kumpulan document yang diupload
doc_uploads = []

def home(request):
    formUpload = FileUploadForm()
    context = {
        'form' : formUpload,
    }
    return render(request, "cosinesimilarity/home.html", context)

def uploadFiles(request):
    global doc_uploads
    formUpload = FileUploadForm()
    doc_uploads = []
    context = {
        'form' : formUpload,
    }
    if request.method == "POST":
        print(request.POST)
        formUpload = FileUploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('uploadfile')
        path_doc = "cosinesimilarity\\static\\cosinesimilarity\\documents\\"
        doc_uploads = []
        for fileindoc in os.listdir(path_doc):
            if not (fileindoc in doc_uploads):
                doc_uploads.append(str(fileindoc))
        print("doc_upload", doc_uploads)
        if formUpload.is_valid():
            for file in files:
                if not(str(file) in doc_uploads):
                    print(file)
                    doc_uploads.append(str(file))
                    instancefile = FileUpload(uploadfile = file)
                    instancefile.save()
    print(doc_uploads)
    return render(request, 'cosinesimilarity/home.html', context)

def searchResult(request):
    global doc_uploads
    text = None
    formUpload = FileUploadForm()
    context = {
        'form' : formUpload
    }
    doc_uploads = []
    path_doc = "cosinesimilarity\\static\\cosinesimilarity\\documents\\"
    for fileindoc in os.listdir(path_doc):
        doc_uploads.append(str(fileindoc))
    
    if request.method == "POST":
        text = request.POST["searchText"]
        context = {
            'cosinesimilarity' : cosine_similarity(text, doc_uploads),
            'form' : formUpload
        }
    return render(request, "cosinesimilarity/home.html", context)

def deleteFiles(request):
    formUpload = FileUploadForm()
    context = {
        'form' : formUpload
    }
    deleteDocuments()
    return render(request, "cosinesimilarity/home.html", context)

def about(request):
    return render(request, "cosinesimilarity/about.html")

def search(request):
    textQuery = ""
    if (request.method == 'POST'):
        textQuery = request.POST['query']
    DIRECTORY = "cosinesimilarity/static/cosinesimilarity/documents/"
    fileName = os.listdir(DIRECTORY)
    contents = cosinesimilarity(textQuery, fileName)
    return render(request, 'cosinesimilarity/search.html', contents)