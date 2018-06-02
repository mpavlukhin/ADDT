from django.shortcuts import render

from addt.views import results
from addt.forms import BiochemicalAnalysisForm
from . services import BiochemicalAnalyzer


# Create your views here.
def index(request):
    form = BiochemicalAnalysisForm()

    if request.method == 'POST':
        filled_form = BiochemicalAnalysisForm(request.POST)
        biochemical_data_dict = filled_form.get_fields()

        analyzer = BiochemicalAnalyzer()
        is_sick = analyzer.process_biochemical_analysis_data(biochemical_data_dict)
        return results(request, is_sick)

    return render(request, 'simple/tool.html', {'form': form})


def deep(request):
    form = BiochemicalAnalysisForm()

    if request.method == 'POST':
        filled_form = BiochemicalAnalysisForm(request.POST)
        biochemical_data_dict = filled_form.get_fields()

        analyzer = BiochemicalAnalyzer()
        is_sick, conclusion = analyzer.deep_process_biochemical_analysis_data(biochemical_data_dict)
        return results(request, is_sick, conclusion)

    return render(request, 'simple/tool.html', {'form': form})
