from django.shortcuts import render

from addt.forms import BiochemicalAnalysisForm
from addt.services import BiochemicalAnalysisForm_get_fields


# Create your views here.
def index(request):
    form = BiochemicalAnalysisForm()

    if request.method == 'POST':
        BiochemicalAnalysisForm_get_fields(request, form)

    #blah blah encode parameters for a url blah blah
    #and make another post request
    #edit : added ": "  after    if request.method=='POST'

    return render(request, 'simple/tool.html', {'form': form})