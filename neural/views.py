from django.shortcuts import render

from addt.views import results
from . services import ConvolutionalNeuralNetworkAnalyzer
from . forms import UploadAnimalImageForm


# Create your views here.
def index(request):
    form = UploadAnimalImageForm()

    if request.method == 'POST' and request.FILES['image']:
        filled_form = UploadAnimalImageForm(request.POST, request.FILES)
        # if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
        print(request.POST)
        print(request.FILES['image'])

        analyzer = ConvolutionalNeuralNetworkAnalyzer()
        # is_sick, conclusion = analyzer.process_biochemical_analysis_data(biochemical_data_dict)
        # return results(request, is_sick, conclusion)

    return render(request, 'neural/tool.html', {'form': form})
