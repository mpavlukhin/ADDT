from django import forms
from django.conf import settings

class UploadAnimalImageForm(forms.Form):
    ANIMAL_CHOICES = settings.ANIMAL_CHOICES

    animal = forms.ChoiceField(choices=ANIMAL_CHOICES)
    image = forms.FileField(label='Image:')

    def get_fields(self):
        if self.is_valid():
            form_data_dict = self.cleaned_data
            return form_data_dict
