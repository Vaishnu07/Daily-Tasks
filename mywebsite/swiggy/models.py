from django.db import models
# Create your models here.
class category (models.Model):
    coldbeverage = models.CharField(max_length=250)
    Breakfast = models.IntegerField (default=0)
    SpecialDosavarieties = models.IntegerField(default=0)
    Ravadosas = models.IntegerField(default=0)
class food (models.Model):
    food = models.CharField(max_length=250)
    image = models.ImageField (null=True, blank= True,upload_to='media/')
    quentity = models.IntegerField (default=0)
    price = models.IntegerField(default=0)
    # description = models.CharField(max_length=250)
  
   

