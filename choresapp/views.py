from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Provider, Client, Transaction, Category
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the chores index.")

def client_register(request):
    return render(request, 'choresapp/client/registration.html')

def provider_register(request):
    return HttpResponse("Form to register Providers")

def client_home(request):
    transaction_list = Transaction.objects.order_by('finish_time')
    context = {'transaction_list': transaction_list}
    return render(request, 'choresapp/client/index.html', context)

def provider_home(request):
    transaction_list = Transaction.objects.order_by('finish_time')
    context = {'transaction_list': transaction_list}
    return render(request, 'choresapp/provider/index.html', context)

def trans_detail(request, trans_id):
    transaction = get_object_or_404(Transaction, id=trans_id)
    context = {'transaction': transaction}
    return render(request, 'choresapp/trans/index.html', context)
