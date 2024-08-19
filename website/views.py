from django.shortcuts import render, redirect
from .models import Customer
from .forms import Customerform
from django.contrib import messages

# Create your views here.
def home(request):
    all_customers = Customer.objects.all()
    return render(request, 'home.html', {'all': all_customers})

def join(request):
    if request.method == "POST":
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Form Has Been Submitted Successfully!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your form! Please try again.')
            return render(request, 'join.html', {'form': form})  # Return the form with errors

    else:
        form = Customerform()  # Send an empty form on GET request
    return render(request, 'join.html', {'form': form})
