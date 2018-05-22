from django.shortcuts import render

from addt.forms import BiochemicalAnalysisForm
from . services import BiochemicalAnalyzer


# Create your views here.
def index(request):
    form = BiochemicalAnalysisForm()

    if request.method == 'POST':
        filled_form = BiochemicalAnalysisForm(request.POST)
        biochemical_data_dict = filled_form.get_fields()

    return render(request, 'simple/tool.html', {'form': form})