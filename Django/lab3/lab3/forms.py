from django import forms

class SubmitUrlform(forms.Form):
    url = forms.CharField(label='Submit URL')