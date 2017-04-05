from django.contrib import admin
from mpesa.models import Customer
from mpesa.models import Transaction

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('firstname','surname','identification', 'phone_number', 'balance', 'date_of_birth')

admin.site.register(Customer, CustomerAdmin)

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('customer_name', 'amount', 'transaction_type', 'cost', 'date_of_transaction', 'transaction_id')

admin.site.register(Transaction, TransactionAdmin)

