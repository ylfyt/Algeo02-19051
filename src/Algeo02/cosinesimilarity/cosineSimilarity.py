# import packages
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from stop_words import get_stop_words
import io
import re

def cosine_similarity(text):
    output = None
    return output

def stemmingDokumen(dokumen):
    #Membuat stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    #Array yang menyimpan stopword dalam Bahasa Indonesia
    stopwords = get_stop_words('indonesian') + get_stop_words('english')

    #Membuka, membaca, dan menutup dokumen
    f = open(dokumen, "r")
    dokumen = f.readlines()
    f.close()

    #Membersihkan dokumen dari karaker yang tidak diperlukan
    hasilDokumen = ""
    for kata in dokumen:
        hasilDokumen += kata + " "
    hasilDokumen = re.split(' |\n|#|-',hasilDokumen)

    #Menghapus stopword yang ada di dokumen
    hasilNoStopword = []
    for i in range(len(hasilDokumen)):
        bukanStopword = True
        for kata in stopwords:
            if(hasilDokumen[i] == kata):
                bukanStopword = False
        if (bukanStopword and hasilDokumen[i] != ""):
            hasilNoStopword.append(hasilDokumen[i])

    #Melakukan stemming di setiap kata    
    for i in range(len(hasilNoStopword)):
        hasilNoStopword[i] = stemmer.stem(hasilNoStopword[i])

    #Menghapus stopword kedua kalinya
    hasilNoStopword2 = []
    for i in range(len(hasilNoStopword)):
        bukanStopword = True
        for kata in stopwords:
            if(hasilNoStopword[i] == kata):
                bukanStopword = False
        if (bukanStopword and hasilNoStopword[i] != ""):
            hasilNoStopword2.append(hasilNoStopword[i])

    return hasilNoStopword2

def stemmingQuery(dokumen):
    #Membuat stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    #Array yang menyimpan stopword dalam Bahasa Indonesia
    stopwords = get_stop_words('indonesian') + get_stop_words('english')

    #Membuka query
    dokumen = re.split(' ', dokumen)

    #Membersihkan dokumen dari karaker yang tidak diperlukan
    hasilDokumen = ""
    for kata in dokumen:
        hasilDokumen += kata + " "
    hasilDokumen = re.split(' |\n|#|-',hasilDokumen)

    #Menghapus stopword yang ada di dokumen
    hasilNoStopword = []
    for i in range(len(hasilDokumen)):
        bukanStopword = True
        for kata in stopwords:
            if(hasilDokumen[i] == kata):
                bukanStopword = False
        if (bukanStopword and hasilDokumen[i] != ""):
            hasilNoStopword.append(hasilDokumen[i])

    #Melakukan stemming di setiap kata    
    for i in range(len(hasilNoStopword)):
        hasilNoStopword[i] = stemmer.stem(hasilNoStopword[i])

    #Menghapus stopword kedua kalinya
    hasilNoStopword2 = []
    for i in range(len(hasilNoStopword)):
        bukanStopword = True
        for kata in stopwords:
            if(hasilNoStopword[i] == kata):
                bukanStopword = False
        if (bukanStopword and hasilNoStopword[i] != ""):
            hasilNoStopword2.append(hasilNoStopword[i])

    return hasilNoStopword2


