from django.db import models

class Contact(models.Model):
	firstName = models.CharField(max_length=25)
	lastName = models.CharField(max_length=50)
	companyName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phoneNumber = models.CharField(max_length=14)


	def __str__(self):
		return self.firstName + " " + self.lastName + " | " + self.companyName