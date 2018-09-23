import json
from .models import Banknote
from .utils import withdraw_money
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


def bank_status(request):
    all_banknotes = Banknote.objects.all()
    context_data = {}
    if all_banknotes.exists():
        for note in all_banknotes.iterator():
            context_data[note.denominator] = note.quantity

    return HttpResponse(json.dumps(context_data), content_type='application/json')


@csrf_exempt
def bank_set(request):
    data = json.loads(request.body)
    Banknote.objects.all().delete()
    for note, value in data.items():
        try:
            note = int(note)
            value = int(value)
            positive = note > 0 and value > 0
            if not positive:
                raise Http404("Banknotes entered should be larger than 0")

            Banknote.objects.create(denominator=note, quantity=value)
        except ValueError:
            Banknote.objects.all().delete()
            raise Http404("Invalid banknotes entered")
    return HttpResponse(status=201)


@csrf_exempt
def withdraw(request):
    data = json.loads(request.body)
    all_banknotes = Banknote.objects.all()
    notes = {}
    if all_banknotes.exists():
        for note in all_banknotes.iterator():
            notes[note.denominator] = note.quantity

    result = withdraw_money(notes, data['amount'])
    if result:
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        raise Http404("Could not get exact amount")
