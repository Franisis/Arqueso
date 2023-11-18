from django.shortcuts import render
from .logic import results_logic as rl
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .forms import resultsForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def resultGet(request):
    if request.method=='GET':
        results = rl.get_results()
        results_dto = serializers.serialize('json', results)
        return HttpResponse(results_dto, "application/json" )
    
    pass

def resultPost(request):
    if request.method=='POST':
        form = resultsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Succesfully created results')
            return HttpResponseRedirect(reverse('resultPost'))
        else: print(form.errors)
    else:
        form = resultsForm()
    context = {'form': form,}
    return HttpResponse(context)

