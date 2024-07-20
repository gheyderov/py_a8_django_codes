from django import forms
from products.models import RecipeReview

class ReviewForm(forms.ModelForm):

    class Meta:
        model = RecipeReview
        fields = [
            'message'
        ]
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message',
                'rows' : 7,
                'cols' : 30
            })
        }