from django import forms
from app_nomad.models import Coworking, Accommodation

class PostCoworking(forms.ModelForm):
    class Meta:
        model = Coworking
        fields = ('name', 'location', 'phone_number', 'url', 'content', 'region')

class PostAccommodation(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ('name', 'location', 'phone_number', 'url', 'content', 'region', 'near_coworking_spaces')