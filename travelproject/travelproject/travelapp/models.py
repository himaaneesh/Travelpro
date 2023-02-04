from django.db import models

# Create your models here.
class choose(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='mypics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='mypics')
    desc1=models.TextField()

    def __str__(self):
        return self.name1



