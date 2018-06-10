from django.shortcuts import render

from addt.views import results
from . services import ConvolutionalNeuralNetworkAnalyzer
from . forms import UploadAnimalImageForm


# Create your views here.
def index(request):
    form = UploadAnimalImageForm()

    if request.method == 'POST' and request.FILES['image']:
        filled_form = UploadAnimalImageForm(request.POST, request.FILES)
        form_data_dict_for_neural_net = filled_form.get_fields()
        
        temporary_image = request.FILES['image']
        temporary_image_path = temporary_image.temporary_file_path()

        analyzer = ConvolutionalNeuralNetworkAnalyzer()
        is_sick, conclusion = analyzer.process_biochemical_analysis_data(
            form_data_dict_for_neural_net, temporary_image_path)
        return results(request, is_sick, conclusion)

    return render(request, 'neural/tool.html', {'form': form})
