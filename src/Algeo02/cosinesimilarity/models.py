from django.db import models

# Create your models here.
class FileUpload(models.Model):
   uploadfile = models.FileField(upload_to='cosinesimilarity/static/cosinesimilarity/documents', null=True, blank=True)