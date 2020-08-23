from django.db import models

class UserAddress(models.Model) :
    home_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self) :
        return self.home_no

class UserInfo (models.Model) :
    userid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    useraddress = models.ForeignKey('UserAddress', on_delete=models.CASCADE)

    def __str__(self) :
        return self.username
