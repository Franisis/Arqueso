import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .logic import users_logic as ul
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MedicalProfessionalForm, PatientForm
from django.http import QueryDict
# Create your views here.

def userGet(request):
    if request.method=='GET':
        users = ul.get_users()
        users_dto = serializers.serialize('json', users)
        return HttpResponse(users_dto, 'application/json')
    
def userPut(request):

    if request.method=='POST':
        print("avafvojebjbewnjbnejkbnljeskbnl",request.body)
        body_unicode = request.body.decode('utf-8')
        body_data = QueryDict(body_unicode)

        # Access the values
        id = body_data.get('identification')
        rol = body_data.get('role')

        print("SEXOOOOOOOOOOOOOOOOOOANALLLLLLLLLLLLLLLLLLLLL",id, rol)
        
        user_dto = ul.update_rol(id, rol)
        print(user_dto)
        user = serializers.serialize('json', [user_dto,])
        return HttpResponse(user, 'application/json')
        
    else:
        form = PatientForm()
        render(request, 'userCreate.html', {'form': form})

def userPutPage(request):
    if request.method=='GET':
        return render(request, 'userCreate.html')
    
def userPost(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully created User')
            return HttpResponseRedirect(reverse('userCreate'))
        elif MedicalProfessionalForm(request.POST).is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully created User')
            return HttpResponseRedirect(reverse('userCreate'))
        else:
            print(form.errors)
    else:
        form = PatientForm()
    context={'form':form,}
    return HttpResponse(context)


