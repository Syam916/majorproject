from django.db import models

# Create your models here.
class NaturalConvection(models.Model):
    current=models.CharField(max_length=10)
    voltage=models.CharField(max_length=10)
    power=models.CharField(max_length=10)

    Temperature_2=models.CharField(max_length=10)
    Temperature_3=models.CharField(max_length=10)
    Temperature_4=models.CharField(max_length=10)
    Temperature_5=models.CharField(max_length=10)
    Temperature_6=models.CharField(max_length=10)
    Ambient_Temperature=models.CharField(max_length=10)
    theoritical_output=models.CharField(max_length=10)
    experimental_output=models.CharField(max_length=10)


    

    
    
    
