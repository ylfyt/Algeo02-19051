from django.http import request
from django.shortcuts import render
from .cosineSimilarity import cosine_similarity, stemmingDokumen, stemmingQuery
# Create your views here.


def home(request):
    return render(request, "cosinesimilarity/home.html")

def searchResult(request):
    text = request.POST["searchText"]
    context = {
        'cosinesimilarity' : stemmingQuery(text),
    }
    return render(request, "cosinesimilarity/home.html", context)

def about(request):
    return render(request, "cosinesimilarity/about.html")

