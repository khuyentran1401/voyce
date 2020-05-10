from django.db import models

# Class attributes correspond to columns 
# Instances of the classes correspond to rows in the database. 

# Create your models here.
class Table(models.Model):
	facility = models.CharField(max_length=200)
	type = models.CharField(max_length=20)
	number_beds = models.IntegerField()
	region = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=5)
	zip = models.IntegerField()
	telefone = models.CharField(max_length=200)
	fax = models.CharField(max_length=200)
	admin = models.CharField(max_length=200)
	admin_email = models.EmailField()
	sw = models.CharField(max_length=200)
	sw_email = models.EmailField()
	markt = models.CharField(max_length=200)
	markt_email = models.EmailField()

