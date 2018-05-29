from django.shortcuts import render


# Create your views here.
def results(request, is_sick, conclusion=str()):
    return render(request, 'results.html', {'is_sick': is_sick, 'conclusion': conclusion})
