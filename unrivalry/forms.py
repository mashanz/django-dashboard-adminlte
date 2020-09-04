from django import forms


class AddPersonForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control"
            }
        )
    )

    shirt_size = forms.CharField(
        widget=forms.ChoiceField()
    )
