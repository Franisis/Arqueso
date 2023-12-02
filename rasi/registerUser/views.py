from django.shortcuts import render
from .logic import registerUser_logic as rl
from .forms import registerUserForm 
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from rasi.auth0backend import getRole

# Create your views here.

def registers_userView(request):
    role=getRole(request)
    if request.method == 'GET' and role=='admin':
        registers = rl.get_registers()
        registers_dto= serializers.serialize('json', registers)
        return HttpResponse(registers, 'application/json')
    if request.method=='POST':
        form = registerUserForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Successfully created variable')
            form.save()
            return HttpResponseRedirect(reverse('registerCreate'))
        else:
            print(form.errors)
    else:
        form = registerUserForm()
    context = {
        'form': form,
    }
    return HttpResponse("m3w")


