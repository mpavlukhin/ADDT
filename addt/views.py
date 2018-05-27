from django.shortcuts import render


# Create your views here.
def results(request, is_sick):
    return render(request, 'results.html', {'is_sick': is_sick})
