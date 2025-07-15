from django import forms

class IngredientForm(forms.Form):
    ingredients = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": 4,
            "class": "form-control",
            "placeholder": "e.g. Tamarind paste, Goat cheese, Sumac powder"
        })
    )
