import math
import os
from .stemming import stemmingDokumen, stemmingQuery

def cosinesimilarity(textQuery, fileName):

	DIRECTORY = "cosinesimilarity/static/cosinesimilarity/documents/"

	title = []
	firstSentence = []
	for i in range(len(fileName)):
		path = DIRECTORY + fileName[i]
		f = open(path, 'r')
		# for title
		s = f.readline()
		title.append(s[1:])
		# for first sentence
		s = f.readline()
		firstSentence.append(s)


	docs = []
	query = stemmingQuery(textQuery)
	if (len(query) != 0):
		docs.append(query)
		for i in range(len(fileName)):
			path = DIRECTORY + fileName[i]
			stemDoc = stemmingDokumen(path)
			docs.append(stemDoc)

	n = len(docs)
	vectors = [[] for i in range(n)]

	if (n > 1 and len(query) != 0):
		terms = []
		for doc in docs:
			for word in doc:
				if (word not in terms):
					terms.append(word)
					for i in range(n):
						a = countWord(word, docs[i])
						vectors[i].append(a)

	
		sim = [0 for i in range(n-1)]
		for i in range(n-1):
			vectorQ = vectors[0]
			vectorDoc = vectors[i+1]
			lenQ = lenVec(vectorQ)
			lenD = lenVec(vectorDoc)

			cos = float(dotProduct(vectorQ, vectorDoc) / (lenQ * lenD))
			sim[i] = cos

		rank = [i for i in range(n-1)]
		for i in range(n-1):
		    idxMax = i
		    for j in range(i+1, n-1):
		        if (sim[rank[j]] > sim[rank[idxMax]]):
		            idxMax = j

		    tmp = rank[i]
		    rank[i] = rank[idxMax]
		    rank[idxMax] = tmp

		nbWord = [len(docs[i]) for i in range(1, n)]

		hasil = []
		for i in range(n-1):
			ans = []
			ans.append(i+1)
			ans.append(fileName[rank[i]])
			ans.append(firstSentence[rank[i]])
			ans.append(title[rank[i]])
			ans.append(int(sim[rank[i]]*100))
			ans.append(nbWord[rank[i]])

			hasil.append(ans)


		table = []
		for i in range(len(query)+1):
			tmp = []
			for j in range(n+1):
				if (i == 0 and j == 0):
					tmp.append("Term")
				elif (i == 0):
					if (j != 1):
						tmp.append("D"+str(j-1))
					else:
						tmp.append("Query")
				elif(j == 0):
					tmp.append(query[i-1])
				else:
					tmp.append(vectors[j-1][i-1])

			table.append(tmp)


		contents = {
		'Error' : False,
		'Table' : table,
		'Ans' : hasil
		}

		return contents
	else:
		contents = {'Error' : True}
		
		return contents





def countWord(w, arr):
	n = 0
	for word in arr:
		if (w == word):
			n += 1
	return n


def lenVec(v):
	a = float(0)
	for i in range(len(v)):
		a += v[i] * v[i]

	return math.sqrt(a)

def dotProduct(v1, v2):
	a = float(0)
	for i in range(len(v1)):
		a += v1[i] * v2[i]

	return a
