from django.db import models
from django.db.models import Model, CASCADE

# Create your models here.

class Users(models.Model):
    Name= models.CharField(max_length=80)
    Email= models.EmailField(max_length=70,blank=True, unique=True)
    Credit = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.Name)


class Transactions(models.Model):
    WhoUsers=models.ForeignKey(to=Users, on_delete=CASCADE, related_name="WhoUser")
    WhomUsers=models.ForeignKey(to=Users, on_delete=CASCADE, related_name="WhomUser")
    Amount = models.IntegerField(blank=True, null=True)
    Status= models.CharField(max_length=80, default="Credit", choices=(("Credit","Credit"),("Debit","Debit")))
    def __str__(self):
        return str(self.WhomUsers)