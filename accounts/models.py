from django.db import models


# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length= 200)
	reg = models.CharField(max_length= 200)
	roll = models.CharField(max_length= 200)
	def __str__(self):
		return self.name
class Login(models.Model):
	mid = models.CharField(max_length= 200)
	pwd = models.CharField(max_length= 200)
	def __str__(self):
		return self.mid
class Sbio(models.Model):
	mid = models.ForeignKey(Login,on_delete=models.CASCADE)
	name = models.CharField(max_length= 200)
	roll = models.CharField(max_length= 200)
	reg = models.CharField(max_length= 200,null=True)
	dob = models.DateField()
	fname = models.CharField(max_length= 200)
	phno = models.CharField(max_length= 200)
	eid = models.CharField(max_length= 200)
	ach = models.TextField()
	rm = models.TextField(null=True)
	def __str__(self):
		return self.name