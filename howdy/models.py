from django.db import models

# Create your models here.
class Address(models.Model):
  name = models.CharField(default="toto",max_length=20,blank=False,null=False)
  email = models.CharField(default="admin@admin",max_length=30,blank=False,null=False)

  def __str__(self):
    return self.name+"  |  "+self.email

  objects = models.Manager()