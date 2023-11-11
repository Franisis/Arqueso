from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .logic import logic_result as lr
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ResultForm



def get_results(request):
    if request.method=='GET':
        results = lr.getResults()
        results_dto = serializers.serialize('json', results)
        return HttpResponse(results_dto, 'application/json')

def createResults(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully created result')
            return HttpResponseRedirect(reverse('resultCreate'))
        else:
            print(form.errors)
    else:
        form = ResultForm()
    context={'form': form,}
    return HttpResponse(context)

        
    
# Create your views here.
