from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=50,default='orders')
    
    def getstatus():
        return Status.objects.all()

    def __str__(self):
       return self.name