from django.db import models


class advertisement(models.Model):
    brief = models.TextField(blank=True,null=True)
    advertisement = models.ImageField(upload_to='uploads/product_images/')


    def getadds():
        return advertisement.objects.all()

    