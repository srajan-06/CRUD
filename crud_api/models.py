from django.db import models

class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, blank= True)
    phone = models.CharField(max_length=10,blank=True)
    age = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

