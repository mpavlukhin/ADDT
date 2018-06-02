from copy import deepcopy
from django.conf import settings


class ConvolutionalNeuralNetworkAnalyzer:
    animals = None

    def __init__(self):
        self.animals = settings.ANIMALS

    def process_biochemical_analysis_data(self, data_dict):
        is_sick = False
        conclusion = 'No'
        animal = data_dict['animal']

        return is_sick, conclusion