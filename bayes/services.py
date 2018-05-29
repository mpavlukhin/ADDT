from sklearn.naive_bayes import GaussianNB, MultinomialNB
import numpy as np
import random
import re
from csv import reader

from django.conf import settings

class NaiveBayesClassifier:
    animals = None

    def __init__(self):
        self.animals = settings.ANIMALS

    def process_biochemical_analysis_data(self, data_dict):
        animal = data_dict['animal']

        with open('bayes/data/{0:s}_dataset.csv'.format(animal)) as csvfile:
            read_csv = reader(csvfile, delimiter=',')

            x = [row[0:11] for row in read_csv]
            x = np.array(x, float)

            csvfile.seek(0)
            y = [row[11] for row in read_csv]
            y = np.array(y)

            model = MultinomialNB()

            model.fit(x, y)

            predicted = model.predict([[data_dict['aspat'], data_dict['alt'], data_dict['ck'], data_dict['ggt'],
                                       data_dict['ph'], data_dict['cl'], data_dict['trig'], data_dict['tc'],
                                       data_dict['alb'], data_dict['ca'], data_dict['fe']]] )
            
            conclusion = predicted[0]

            if conclusion == 'healthy':
                is_sick = False
                return is_sick, conclusion

            is_sick = True
            return is_sick, conclusion


    def generate_dataset(self):
        for animal in self.animals:
            with open('bayes/data/{0:s}_dataset.csv'.format(animal), 'a') as f:
                for i in range(0, 100000):
                    is_sick_data = bool(random.getrandbits(1))

                    if not is_sick_data:
                        results = NaiveBayesClassifier.generate_normal_results()
                        conclusion = 'healthy'

                    else:
                        if animal == 'horse':
                            results = NaiveBayesClassifier.generate_normal_results()
                            results = list(results)

                            disease_choose = random.randint(0, 10)
                            increase_choose = bool(random.getrandbits(1))

                            if disease_choose == 0:
                                if increase_choose:
                                    results[0] = random.uniform(301, 350)
                                    conclusion = 'necrosis of liver cells'

                                else:
                                    results[0] = random.uniform(100, 129)

                            if disease_choose == 1:
                                if increase_choose:
                                    results[1] = random.uniform(21, 30)
                                    conclusion = 'cholangitis'

                                else:
                                    results[1] = random.uniform(1, 2.6)

                            if disease_choose == 2:
                                if increase_choose:
                                    results[2] = random.uniform(301, 320)
                                    conclusion = 'myocardial infarction'

                                else:
                                    results[2] = random.uniform(30, 49)

                            if disease_choose == 3:
                                if increase_choose:
                                    results[3] = random.uniform(21, 30)
                                    conclusion = 'hepatitis'

                                else:
                                    results[3] = random.uniform(0, 0.9)

                            if disease_choose == 4:
                                if increase_choose:
                                    results[4] = random.uniform(7.46, 8)
                                    conclusion = 'alkalosis'

                                else:
                                    results[4] = random.uniform(7, 7.34)
                                    conclusion = 'acidosis'

                            if disease_choose == 5:
                                if increase_choose:
                                    results[5] = random.uniform(107, 110)
                                    conclusion = 'hypohydration'

                                else:
                                    results[5] = random.uniform(86, 93)
                                    conclusion = 'hypochloraemic alkalosis'

                            if disease_choose == 6:
                                if increase_choose:
                                    results[6] = random.uniform(0.4, 1)
                                    conclusion = 'hyperlipoproteinemia'

                                else:
                                    results[6] = random.uniform(0, 0.09)
                                    conclusion = 'hyperthyroidism'

                            if disease_choose == 7:
                                if increase_choose:
                                    results[7] = random.uniform(3.7, 4.2)
                                    conclusion = 'hyperlipoproteinemia'

                                else:
                                    results[7] = random.uniform(1.8, 2.3)
                                    conclusion = 'hypoproteinemia'

                            if disease_choose == 8:
                                if increase_choose:
                                    results[8] = random.uniform(3.7, 4.2)
                                    conclusion = 'dehydration'

                                else:
                                    results[8] = random.uniform(1.8, 2.3)
                                    conclusion = 'alimentary dystrophy'

                            if disease_choose == 9:
                                if increase_choose:
                                    results[9] = random.uniform(4, 4.6)
                                    conclusion = 'hyperparathyroidism'

                                else:
                                    results[9] = random.uniform(2, 2.6)
                                    conclusion = 'hypoparathyroidism'

                            if disease_choose == 10:
                                if increase_choose:
                                    results[9] = random.uniform(23, 30)
                                    conclusion = 'hemosiderosis'

                                else:
                                    results[9] = random.uniform(6, 13)
                                    conclusion = 'iron-deficiency anemia'

                        f.write('{0}{1}\n'.format(re.sub('[()\[\] ]+', '', results.__str__()), (',' + conclusion)))


    @staticmethod
    def generate_normal_results():
        aspat = random.uniform(130, 300)
        alt = random.uniform(2.7, 20)
        ck = random.uniform(50, 300)
        ggt = random.uniform(1, 20)
        ph = random.uniform(7.35, 7.45)
        cl = random.uniform(94, 106)
        trig = random.uniform(0.1, 0.4)
        tc = random.uniform(2.3, 3.6)
        alb = random.uniform(27, 37)
        ca = random.uniform(2.6, 4)
        fe = random.uniform(13, 23)

        return aspat, alt, ck, ggt, ph, cl, trig, tc, alb, ca, fe