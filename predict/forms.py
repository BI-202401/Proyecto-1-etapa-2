from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'review',
        ]
        labels = {
            'review': 'Escriba su reseña',
        }
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }
        initial = {'classification': 5}
