from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def client_form(request):
   if request.method == "POST":
       form = CustomerForm(request.POST)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.created_date = timezone.now()
           customer.save()
           customers = Customer.objects.filter(created_date__lte=timezone.now())
           messages.success(request, 'The client is successfully registered!')
           #return render(request, 'clients/customer_form.html', {'customer': customer})
           form = CustomerForm()
       else:
            messages.add_message(request, messages.ERROR, 'Please Complete All Fields To Submit Your Registration.')
   else:
       form = CustomerForm()
       #messages.error(request, 'The registration of the client was not completed successfully!')
       # print("Else")
   return render(request, 'clients/client_form.html', {'form': form})

@login_required
def client_list(request):
    client = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'clients/client_list.html',
                 {'clients': client})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=client)
       if form.is_valid():
           client = form.save(commit=False)
           client.updated_date = timezone.now()
           client.save()
           client = Customer.objects.filter(created_date__lte=timezone.now())
           messages.success(request, 'The client information is successfully updated!')
           return redirect('clients:client_list')
    else:
        # edit
       form = CustomerForm(instance=client)
    return render(request, 'clients/client_edit.html', {'form': form})

@login_required
def client_delete(request, pk):
   client = get_object_or_404(Customer, pk=pk)
   client.delete()
   messages.success(request, 'The client is successfully deleted!')
   return redirect('clients:client_list')
