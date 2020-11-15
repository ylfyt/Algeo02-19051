import os

def deleteDocuments():
    path = "cosinesimilarity\\static\\cosinesimilarity\\documents\\"
    for delete in os.listdir(path):
        paths = os.path.join(path, delete)
        os.remove(paths)

def conv_txt_to_html(files):
	DIRECTORY = "cosinesimilarity/static/cosinesimilarity/documents/"
	DIRHTML = "cosinesimilarity/templates/cosinesimilarity/documents/"
	for file in files:
		with open(DIRECTORY + file, "r") as rf:
			with open(DIRHTML + file[:-4] + ".html", "w") as wf:
				wf.write("<!DOCTYPE html>\n<html>\n<head>\n")
				f_read = True
				first_title = True
				t = "	"
				while f_read:
					f_read = rf.readline()
					if "#" in f_read:
						if first_title:
							wf.write(t+"<title>" + f_read[1:-1] + "</title>\n")
							wf.write(t+'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">\n')
							wf.write("</head>\n<body>\n")
							wf.write(t+'<div class="container mt-5">\n')
							wf.write(t+t+'<h3 style="text-align: center;">' + f_read[1:-1] + "</h3>\n")
							wf.write(t+t+"<hr>\n")
							first_title = False
						else:
							wf.write(t+t+"<h4>" + f_read[1:-1] + "</h4>\n")
					else:
						wf.write(t+t+"<p>" + f_read[:-1] + "</p>\n")
				wf.write(t+t+'<hr>\n')
				wf.write(t+t+'<a href="/about" class="btn btn-info">Perihal</a>\n')
				wf.write(t+'</div>\n')
				wf.write('</body>\n')
				wf.write('</html>\n')
				#