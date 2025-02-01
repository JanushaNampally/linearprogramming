from django import forms 
class LPForm(forms.Form):
    equations = forms.CharField(widget=forms.Textarea, required=True)