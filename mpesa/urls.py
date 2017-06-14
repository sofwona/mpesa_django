from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'mpesa'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	# /views/transaction
	url(r'^(?P<transaction_id>[0-9]+)/$' , views.detail, name='detail'),
	# /views/amount
	url(r'^(?P<transaction_id>[0-9]+)/amount/$', views.amount, name='amount'),
	# /views/submit/
	url(r'^(?P<transaction_id>[0-9]+)/submit/$', views.submit, name='submit'),
	# /views/statements/
	url(r'^(?P<transaction_id>[0-9]+)/statements/$', views.statements),
	# generic views
	url(r'^detail/$', TemplateView.as_view(template_name="detail.html")),
]