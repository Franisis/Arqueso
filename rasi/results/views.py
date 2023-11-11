from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .logic import logic_result as lr
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect



def get_results(request):
    if request.method=='GET':
        results = lr.getResults()
        results_dto = serializers.serialize('json', results)
        return HttpResponse(results_dto, 'application/json')

# Create your views here.
