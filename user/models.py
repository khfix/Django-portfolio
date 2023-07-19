from django.db import models



class Me(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='photos/')
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    cv = models.FileField(upload_to='cv/')
    

    