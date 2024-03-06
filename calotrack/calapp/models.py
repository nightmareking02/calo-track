from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class calmodel(models.Model):
    name=models.CharField( max_length=50)
    quantity= models.FloatField()
    protien=models.FloatField()
    carbs=models.FloatField()
    fat=models.FloatField()
    nutrients=models.FloatField()
    vitamins= models.CharField(max_length=50)
    img= models.ImageField(upload_to='media',blank=True)
    type= models.CharField(max_length=50)
    favourite=models.ManyToManyField(User,related_name='favourites',blank=True,default=False)
    def __str__(self):
        return (self.name)
    

class savemodel(models.Model):
    consumedfood=models.ForeignKey(calmodel,on_delete=models.CASCADE)
    quantity= models.FloatField()


class finalmodel(models.Model):
    name=models.CharField( max_length=50)
    quantity= models.FloatField()
    protien=models.FloatField()
    carbs=models.FloatField()
    fat=models.FloatField()
    nutrients=models.FloatField()
    vitamins= models.CharField(max_length=50)
    img= models.ImageField(upload_to='foodimg/',blank=True)
    type= models.CharField(max_length=50)

    
