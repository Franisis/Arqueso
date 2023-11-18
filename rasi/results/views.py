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
from social_core.backends.oauth import BaseAuth
from rasi.settings import LOGIN_REDIRECT_URL
from rasi.auth0backend import Auth0





# Create your views here.
def resultGet(request):
    print(request)
    if request.method=="GET":
        results = rl.get_results()
        results_dto = serializers.serialize('json', results)
        return HttpResponse(results_dto, "application/json" )

    
@login_required
def resultPost(request):
    r = Auth0.getRole(request)
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

