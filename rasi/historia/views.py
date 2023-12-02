from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rasi.auth0backend import getRole
from .forms import HistoryForm
from .logic.historia_logic import get_histories, get_history_by_cc

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

@login_required
def get_historias(request):
    """
    params: 
        request: request "GET"
    returns: 
        returns HttpResponse with all histories 
    """
    role = getRole(request)
    if role =="" and request.method=="GET":
        print(request)
        results = get_histories()
        results_dto = serializers.serialize('json', results)
        return HttpResponse

    else:
        return render(request, "indi.html")

        
