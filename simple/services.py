from copy import deepcopy


class BiochemicalAnalyzer:
    normal_results_dict = None
    animals = None
    indicators = None
    normal_results_dict = None

    def __init__(self):
        self.animals = ['horse', ]

        self.indicators = ['aspat', 'alt', 'ck', 'ggt', 'ph',
                           'cl', 'trig', 'tc', 'alb', 'ca', 'fe']
        indicators_dict = {indicator: {'min': None, 'max': None} for indicator in self.indicators}

        self.normal_results_dict = {animal: deepcopy(indicators_dict) for animal in self.animals}

        # Cases
        self.fill_normal_results_dict('horse',
                                      130, 300,
                                      2.7, 20,
                                      50, 300,
                                      1, 20,
                                      7.35, 7.45,
                                      94, 106,
                                      0.1, 0.4,
                                      2.3, 3.6,
                                      27, 37,
                                      2.6, 4,
                                      13, 23)

    def fill_normal_results_dict(self, animal, *indicators_array):
        i = 0
        for indicator in self.indicators:
            for limit in ['min', 'max']:
                self.normal_results_dict[animal][indicator][limit] = indicators_array[i]
                i += 1

    def process_biochemical_analysis_data(self, data_dict):
        is_sick = False
        animal = data_dict['animal']

        for indicator in self.indicators:
            if not(self.normal_results_dict[animal][indicator]['min'] <=
                    data_dict[indicator] <=
                    self.normal_results_dict[animal][indicator]['max']):
                    is_sick = True
                    return is_sick

        return is_sick
