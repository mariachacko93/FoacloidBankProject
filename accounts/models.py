from django.db import models

# Create your models here.
class CreateAccount(models.Model):
    personname=models.CharField(max_length=120)
    accno=models.IntegerField(unique=True)
    acctype=models.CharField(max_length=120)
    balance=models.IntegerField(default=3000)
    phonenumber=models.IntegerField()
    mpin=models.IntegerField(unique=True)

    def __str__(self):
        return self.personname


class Transferdetails(models.Model):
    mpin=models.CharField(max_length=6)
    accno=models.IntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return self.mpin+ self.accno

