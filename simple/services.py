from copy import deepcopy
from django.conf import settings


class BiochemicalAnalyzer:
    normal_results_dict = None
    animals = None
    indicators = None
    normal_results_dict = None

    def __init__(self):
        self.animals = settings.ANIMALS

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
            if not(self.normal_results_dict[animal][indicator]['min'] <
                    data_dict[indicator] <
                    self.normal_results_dict[animal][indicator]['max']):
                    is_sick = True
                    return is_sick

        return is_sick

    def deep_process_biochemical_analysis_data(self, data_dict):
        animal = data_dict['animal']
        conclusion = str()
        is_sick = False

        if data_dict['aspat'] > self.normal_results_dict[animal]['aspat']['max']:
            conclusion += 'necrosis of liver cells '

        if data_dict['alt'] > self.normal_results_dict[animal]['alt']['max']:
            conclusion += 'cholangitis '

        if data_dict['ck'] > self.normal_results_dict[animal]['ck']['max']:
            conclusion += 'myocardial infarction '

        if data_dict['ggt'] > self.normal_results_dict[animal]['ggt']['max']:
            conclusion += 'hepatitis '

        if data_dict['ph'] > self.normal_results_dict[animal]['ph']['max']:
            conclusion += 'alkalosis '

        if data_dict['ph'] < self.normal_results_dict[animal]['ph']['min']:
            conclusion += 'acidosis '

        if data_dict['cl'] > self.normal_results_dict[animal]['cl']['max']:
            conclusion += 'hypohydration '

        if data_dict['cl'] < self.normal_results_dict[animal]['cl']['min']:
            conclusion += 'hypochloraemic alkalosis '

        if data_dict['trig'] > self.normal_results_dict[animal]['trig']['max']:
            conclusion += 'hyperlipoproteinemia '

        if data_dict['trig'] < self.normal_results_dict[animal]['trig']['min']:
            conclusion += 'hyperthyroidism '

        if data_dict['tc'] > self.normal_results_dict[animal]['tc']['max']:
            conclusion += 'hyperlipoproteinemia '

        if data_dict['tc'] < self.normal_results_dict[animal]['tc']['min']:
            conclusion += 'hypoproteinemia '

        if data_dict['alb'] > self.normal_results_dict[animal]['alb']['max']:
            conclusion += 'dehydration '

        if data_dict['alb'] < self.normal_results_dict[animal]['alb']['min']:
            conclusion += 'alimentary dystrophy '

        if data_dict['ca'] > self.normal_results_dict[animal]['ca']['max']:
            conclusion += 'hyperparathyroidism '

        if data_dict['ca'] < self.normal_results_dict[animal]['ca']['min']:
            conclusion += 'hypoparathyroidism '

        if data_dict['fe'] > self.normal_results_dict[animal]['fe']['max']:
            conclusion += 'hemosiderosis '

        if data_dict['fe'] < self.normal_results_dict[animal]['fe']['min']:
                conclusion += 'iron-deficiency anemia '

        if conclusion is not str():
            is_sick = True

        return is_sick, conclusion