from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Client

# Create your views here.

def client_list(request):
    context = {'client_list': Client.objects.all()}
    return render(request, 'client/client_list.html', context)

def client_form(request, id=0):

    if request.method == 'GET':
        if id == 0:
            form = ClientForm()

        else:
            client = Client.objects.get(pk=id)
            form = ClientForm(instance=client)

        return render(request, 'client/client_form.html', {'form': form})
    else:
        if id == 0:
            form = ClientForm(request.POST)

        else:
            client = Client.objects.get(pk=id)
            form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
        return redirect('/client/client_list')

def client_delete(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('/client/client_list')