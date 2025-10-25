from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50)
    age=models.CharField(max_length=50,default="hello")


    def getcategory():
        return Categories.objects.all()

    def __str__(self):
        return self.name