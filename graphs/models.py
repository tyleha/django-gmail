from django.db import models

# Create your models here.

class EmailAccount(models.Model):
	address = models.EmailField(max_length=200)
	password = models.CharField(max_length=200)
	#host = username.split('@')[-1]

	def __unicode__(self):
		return self.address

class Graph(models.Model):
	email = models.ForeignKey(EmailAccount)
	start_date = models.DateField('Start Date')
	end_date = models.DateField('End Date')
	#type
	#image = models.ImageField???

	def __unicode__(self):
		return self.start_date
