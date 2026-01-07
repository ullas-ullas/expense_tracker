from django.shortcuts import render, redirect
from . import models
from django.db.models import Sum

# Create your views here.

def homeFn(request):
    if request.method == "POST":
        print(request.POST)
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        models.Transaction.objects.create(description = description , amount = amount)
        return redirect('homepage')
    transaction_sum = models.Transaction.objects.all().aggregate(Sum('amount'))['amount__sum']
    if transaction_sum is None:
        transaction_sum = 0
    all_transactions = models.Transaction.objects.all()

    print(transaction_sum)
    return render(request,'home.html', {'transaction_sum': transaction_sum, 'transaction_objs': all_transactions})
