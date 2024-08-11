from django.db import models


# Create your models here.
class OrmModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    sal = models.IntegerField()