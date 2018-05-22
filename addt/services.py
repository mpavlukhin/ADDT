from django.shortcuts import render

from addt.forms import BiochemicalAnalysisForm


def BiochemicalAnalysisForm_get_fields(request, form):
        form = BiochemicalAnalysisForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            animal = cd.get('animal')
            print(cd)