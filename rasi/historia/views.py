from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from rasi.auth0backend import getRole
from .forms import HistoryForm

# Create your views here.


@login_required
def create_historia(request):
    role = getRole(request)
    if role =="medic":
        print(request)
        if request.method=="POST":
            form = HistoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Succesfully created results')
            return HttpResponseRedirect(reverse('historyCreate'))

    pass