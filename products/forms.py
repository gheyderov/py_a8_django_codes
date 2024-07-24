from django import forms
from products.models import RecipeReview, Recipe

class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'title',
            'small_description',
            'description',
            'cover_image',
            'category',
            'tags'
        ]
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'small_description' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'description' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control'
            }),
            'tags' : forms.SelectMultiple(attrs={
                'class' : 'form-control'
            }),

        }

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


class SubReviewForm(forms.ModelForm):

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