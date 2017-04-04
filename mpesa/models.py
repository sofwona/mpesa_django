from django.db import models
import uuid
# Create your models here.

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
	phone_number = models.ForeignKey(
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

class Customer(models.Model):
	firstname = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	identification = models.CharField(max_length=20)
	phone_number = models.PositiveIntegerField()
	transaction_id = models.CharField(max_length=7)
	balance = models.IntegerField()
