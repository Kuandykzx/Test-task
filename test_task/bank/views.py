from django.shortcuts import render
# from django.views.generic import TemplateView, DetailView
from .models import Banknote
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
import json


def bank_status(request):
    all_banknotes = Banknote.objects.all()
    context_data = {}
    if all_banknotes.exists():
        # Another database query to start fetching the rows in batches.
        for note in all_banknotes.iterator():
            context_data[note.denominator] = note.quantity

    return HttpResponse(json.dumps(context_data), content_type='application/json')


def bank_set(request):
    print(request.data)
    for k,v in request.data:
        print(k,v)