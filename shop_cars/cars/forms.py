from django import forms
from .models import Car, CarModel, Color, Specifications, Image


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class SpecificationsForm(forms.ModelForm):

    class Meta:
        model = Specifications
        fields = '__all__'


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'
