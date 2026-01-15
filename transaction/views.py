from django.shortcuts import render, redirect
from .models import Transaction
from django.db.models import Sum, Case, When, DecimalField

# Create your views here.

def homeFn(request):
    print(request.user)
    if request.method == "POST":
        print(request.POST)
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        Transaction.objects.create(description = description , amount = amount)
        return redirect('transaction:homepage')
    transaction_sum = Transaction.objects.all().aggregate(Sum('amount'))['amount__sum']
    if transaction_sum is None:
        transaction_sum = 0
    total = Transaction.objects.aggregate(
        income = Sum(Case(
            When(amount__gte = 0, then='amount'),
            default=0,
            output_field=DecimalField()
        )),
        expense = Sum(Case(
            When(amount__lt = 0, then='amount'),
            default=0,
            output_field=DecimalField()
        ))
    )
    all_transactions = Transaction.objects.all().order_by('-created_at')

    print(total)

    return render(request,'home.html', {'transaction_sum': transaction_sum, 'transaction_objs': all_transactions, 'income_sum': total['income'], 'expense_sum': total['expense']})

def delete_transaction(request, id):
    item_to_delete = Transaction.objects.filter(pk = id)
    if item_to_delete.exists():
        item_to_delete.delete()
    return redirect('transaction:homepage')
