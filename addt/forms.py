from django import forms


class BiochemicalAnalysisForm(forms.Form):
    ANIMAL_CHOICES = (
        (1, ("Horse")),
    )
    animal = forms.ChoiceField(choices=ANIMAL_CHOICES)
    aspat = forms.IntegerField(label='AspAT')
    ck = forms.IntegerField(label='CK')