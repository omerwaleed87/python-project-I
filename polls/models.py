from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.uid

class Type(models.Model):
    tid = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default="")
    parent = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.tid

class Location(models.Model):
    lid = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    location_key = models.CharField(max_length=200, default="")
    parent = models.IntegerField(default=0)
    def __str__(self):
        return self.lid

class Purpose(models.Model):
    pid = models.CharField(max_length=20, primary_key=True)
    purpose = models.CharField(max_length=20)
    url = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.pid

class Listing(models.Model):
    listId = models.CharField(max_length=20, primary_key=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    price = models.CharField(max_length=200, default="")
    areaCovered = models.CharField(max_length=200, default="")
    areaLand = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=500, default="")
    image = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.listId