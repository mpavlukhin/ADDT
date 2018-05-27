from django import forms


class BiochemicalAnalysisForm(forms.Form):
    ANIMAL_CHOICES = (
        ('horse', ("Horse")),
    )

    animal = forms.ChoiceField(choices=ANIMAL_CHOICES)

    aspat = forms.FloatField(label='AspAT')
    alt = forms.FloatField(label='ALT')
    ck = forms.FloatField(label='CK')
    ggt = forms.FloatField(label='GGT')
    ph = forms.FloatField(label='pH')

    cl = forms.FloatField(label='Cl')
    trig = forms.FloatField(label='Trig')
    tc = forms.FloatField(label='TC')
    alb = forms.FloatField(label='Alb')
    ca = forms.FloatField(label='Ca')
    fe = forms.FloatField(label='Fe')

    def get_fields(self):
        if self.is_valid():
            form_data_dict = self.cleaned_data
            return form_data_dict
