from django.contrib import admin
from mpesa.models import Transaction
from mpesa.models import Customer
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('phone_number', 'amount', 'transaction_type', 'cost', 'date_of_transaction', 'transaction_id')

admin.site.register(Transaction, TransactionAdmin)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('firstname','surname','identification', 'phone_number', 'balance', 'transaction_id')

admin.site.register(Customer, CustomerAdmin)