from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField("Name of Flat Holder", max_length=100)
	email = models.EmailField()
	flat_no = models.CharField("Flat No", max_length=10)
	wing = models.CharField("Wing", max_length=26)
	area = models.CharField("Flat Area", max_length=26)
	mobile = models.IntegerField("Mobile No")

	def __str__(self):
		return self.name

class Bill(models.Model):
	month = models.CharField("Month Of Bill", max_length=20)
	user = models.ForeignKey(Person)
	statement_date = models.DateField()
	due_date = models.DateField()
	sinking_fund = models.IntegerField("Sinking fund")
	repair_and_maintainance = models.IntegerField("Repair and Maintainance")
	water_charges = models.IntegerField("Water Charges")
	electricity_charges = models.IntegerField("Electricity Charges")
	service_charges = models.IntegerField("Service Charges")
	interest = models.IntegerField("Interest rate")
	penalty = models.IntegerField("Penalty")
	adjustments = models.IntegerField("Adjustments")
	unpaid_due = models.IntegerField("Unpaid due")
	payble_amt = models.IntegerField("Total Amount Due")
	total_charges = models.IntegerField("total of charges")
