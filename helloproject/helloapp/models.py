from django.db import models

# Create your models here.
class UserInfo (models.Model) :
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) :
        return self.username
