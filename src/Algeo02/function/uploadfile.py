import os

def cosine_similarity(text, doc_uploads):
    if doc_uploads == []:
        return "The file is empty"
    return doc_uploads

def deleteDocuments():
    path = "cosinesimilarity\\static\\cosinesimilarity\\documents\\"
    for delete in os.listdir(path):
        paths = os.path.join(path, delete)
        os.remove(paths)