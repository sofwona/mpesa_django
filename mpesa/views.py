from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.template import RequestContext
from django.template import Context
from django.views import generic

from .models import Customer, Transaction

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'mpesa/index.html'
	context_object_name = 'latest_transaction_list'

	def get_queryset(self):
		"""Return the last five published transactions. """
		return Transaction.objects.order_by('-pub_date')[:7]

class DetailView(generic.DetailView):
	model = Transaction
	template_name = 'mpesa/detail.html'

class StatementsView(generic.DetailView):
	model = Transaction
	template_name = 'mpesa/statements.html'


def index(request):
	latest_transaction_list = Transaction.objects.order_by('-date_of_transaction')[:5]
	template = loader.get_template('mpesa/index.html')
	context = {
		'latest_transaction_list': latest_transaction_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, transaction_id = '001'):
	try:
		transaction = Transaction.objects.get(pk =transaction_id)
		template = loader.get_template('mpesa/detail.html')
		context = {
		'transaction' : transaction,
		}
		return HttpResponse(template.render(context, request))
	except Transaction.DoesNotExist:
		raise Http404("Tansaction does not exist")
	return render(request, 'mpesa/detail.html', {'transaction': transaction })

def amount(request, transaction_id):
	return HttpResponse("You're looking at the amount for transaction %s." % transaction_id)

def submit(request, transaction_id):
	transaction = get_object_or_404(Transaction, pk= transaction_id)
	try:
		selected_transaction = Transaction.objects.get(pk =transaction_id)
		selected_transaction.save()
		return render(request, 'mpesa/statements.html', {'transaction': transaction})
	except (KeyError, Customer.DoesNotExist):
		return render(request, 'mpesa/detail.html', {
			'transaction': transaction, 
			'error_message': "You didn't select a transaction.",
			})
	return render(request, 'mpesa/statemnts.html', {'transaction': transaction})
	

def statements(request, transaction_id):
	transaction = get_object_or_404(Transaction, pk= transaction_id)
	return render(request, 'mpesa/statements.html', {'transaction': transaction})


