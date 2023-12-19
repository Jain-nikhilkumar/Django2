# from django import forms

# class MyForm(forms.Form):
#     subject = forms.CharField(label='Subject DID', max_length=100)
#     schema_choices = [
#         ('option1', 'Option 1'),
#         ('option2', 'Option 2'),
#         ('option3', 'Option 3'),
#     ]
#     select_schema = forms.ChoiceField(label='Select Schema', choices=schema_choices)
#     expiry_date = forms.DateField(label='Expiry Date', widget=forms.DateInput(attrs={'type': 'date'}))
# myapp/forms.py
from django import forms

class MyForm(forms.Form):
    subject = forms.CharField(label='Subject DID', max_length=100)
    schema_choices = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    select_schema = forms.ChoiceField(label='Select Schema', choices=schema_choices)
    expiry_date = forms.DateField(label='Expiry Date', widget=forms.DateInput(attrs={'type': 'date'}))

class issue_credentials(forms.Form):
    subject = forms.CharField(label='Subject DID', max_length=100)
    schema_choices = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    select_schema = forms.ChoiceField(label='Select Schema', choices=schema_choices)
    expiry_date = forms.DateField(label='Expiry Date', widget=forms.DateInput(attrs={'type': 'date'}))
