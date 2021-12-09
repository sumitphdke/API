from django.db import models

# Create your models here.
class mg(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)
class ss(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    campgain=models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
    