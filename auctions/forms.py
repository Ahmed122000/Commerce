from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta: 
        model=Listing   
        fields = ['title', 'description', 'starting_bid', 'image', 'category', 'end_time']
        widgets = {
            'end_time':forms.DateTimeInput(attrs={'type':'datetime-local'}), 
            'category': forms.CheckboxSelectMultiple() 
        }