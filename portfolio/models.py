from django.db import models # type: ignore

# Create your models here.

class Portfo (models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    university=models.CharField(max_length=50)
    hobby=models.TextField(max_length=300)
    skills=models.TextField(max_length=300)
    work=models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
        