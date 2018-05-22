from django import forms


class BiochemicalAnalysisForm(forms.Form):
    ANIMAL_CHOICES = (
        (1, ("Horse")),
    )

    animal = forms.ChoiceField(choices=ANIMAL_CHOICES)

    aspat = forms.IntegerField(label='AspAT')
    alt = forms.IntegerField(label='ALT')
    ck = forms.IntegerField(label='CK')
    ggt = forms.IntegerField(label='GGT')
    ph = forms.IntegerField(label='pH')

    cl = forms.IntegerField(label='Cl')
    trig = forms.IntegerField(label='Trig')
    tc = forms.IntegerField(label='TC')
    alb = forms.IntegerField(label='Alb')
    ca = forms.IntegerField(label='Ca')
    fe = forms.IntegerField(label='Fe')

    def get_fields(self):
        if self.is_valid():
            form_data_dict = self.cleaned_data
            return form_data_dict
