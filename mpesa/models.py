from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
	firstname = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	identification = models.CharField(max_length=20)
	phone_number = models.PhoneNumberField(primary_key=True)
	date_of_birth = models.DateField(default=datetime.now, blank=True)
	balance = models.IntegerField()

	def __str__ (self):
		return "{} {}". format(self.firstname, self.surname)

class Transaction(models.Model):
	DEPOSIT = 'DP'
	WITHDRAWL = 'WD'

	TYPE_OF_TRANSACTION = (
		(DEPOSIT, 'Deposit'),
		(WITHDRAWL, 'Withdrawl'),
	)


	amount = models.DecimalField(max_digits=9, decimal_places=2)
	date_of_transaction = models.DateTimeField()
	cost = models.DecimalField(max_digits=9, decimal_places=2)
	customer_name = models.ForeignKey(
		'Customer',
		on_delete=models.SET("No transactions."),
	)
	transaction_type = models.CharField(
		max_length=2,
		choices=TYPE_OF_TRANSACTION,
		default=DEPOSIT,
	)
	transaction_id = models.CharField(max_length=20)
	description = models.CharField(max_length=2000)

