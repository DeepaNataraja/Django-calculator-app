from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(label='Enter expression', max_length=255)
