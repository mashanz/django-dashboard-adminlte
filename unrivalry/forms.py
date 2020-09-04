from django import forms
from .models import PersonModel


class AddPersonForm(forms.ModelForm):

    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control"
            }
        )
    )

    shirt_size = forms.CharField(
        widget=forms.Select(
            attrs={
                "name": "shirt_size",
                "placeholder": "Shirt Size",
                "class": "form-control"
            }, choices=SHIRT_SIZES
        )
    )

    class Meta:
        model = PersonModel
        fields = ('full_name', 'shirt_size')
