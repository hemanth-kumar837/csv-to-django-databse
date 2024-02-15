from django.db import models

# Create your models here.
class Business(models.Model):
    Series_reference=models.CharField(max_length=10)
    Period=models.CharField(max_length=10)
    Data_value=models.CharField(max_length=100,null=True,blank=True)
    Suppressed=models.CharField(max_length=100,null=True,blank=True)
    Status=models.CharField(max_length=50)
    Units=models.CharField(max_length=50)
    Magnitude=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=100)
    Series_title_2=models.CharField(max_length=100)
    Series_title_3=models.CharField(max_length=100)

    def __str__(self):
        return self.Series_reference
    