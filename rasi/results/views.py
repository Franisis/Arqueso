from django.shortcuts import render
from .logic import results_logic as rl
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .forms import resultsForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rasi.auth0backend import Auth0
from social_core.backends.oauth import BaseOAuth2

m = BaseOAuth2()

auth0 = Auth0(m)

# Create your views here.
@login_required
def resultGet(request):
        r = auth0.getRole(request)
        if r == "admin" or r =="medic":
            if request.method=="GET":
                results = rl.get_results()
                results_dto = serializers.serialize('json', results)
                return HttpResponse(results_dto, "application/json" )
    
    
@login_required
def resultPost(request):
    r = auth0.getRole(request)
    print(r)
    if r == "medic":
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

