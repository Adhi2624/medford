from django.db import models

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phn_no=models.BigIntegerField()
    subject=models.CharField(max_length=38)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.first_name+" "+self.last_name

class carrer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField(max_length=50,null=True)
    phn_no=models.BigIntegerField()
    resume=models.FileField(null=True,blank=True,upload_to="resumes/")
    message=models.TextField(max_length=500,null=True)
    

    def __str__(self):
        return self.first_name+" "+self.last_name