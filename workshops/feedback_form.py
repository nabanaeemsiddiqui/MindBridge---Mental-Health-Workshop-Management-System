from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:

        model = Feedback

        fields = ['rating', 'comment']

        widgets = {

            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5
            }),

            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }