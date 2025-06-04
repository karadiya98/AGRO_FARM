from django.db import models

class User_Detail(models.Model):
    user_id = models.AutoField(primary_key=True)  # Automatically generated, unique ID
    user_name = models.CharField(max_length=100)
    gmail = models.CharField(max_length=255)
    password = models.IntegerField()  # Removed max_digits for IntegerField
    confirm_password = models.IntegerField()  # Removed max_digits for IntegerField

    
