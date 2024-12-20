from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name+" "+str(self.age)
class Games(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=100)

    def __str__(self):
        return self.name+" "+str(self.description)
