from django import forms

class BillForm(forms.Form):
    month = forms.DateField(label='Month')
    statement_date = forms.DateField()
    due_date = forms.DateField()
    sink_fund= forms.DecimalField(label='Sinking Fund')
    repair = forms.DecimalField(label='Repairs & Maintainance')
    water_charges = forms.DecimalField(label='Water Charges')
    electricity_charges = forms.DecimalField(label='Electricity Charges')
    service_charges = forms.DecimalField(label='Service Charges')
    interest = forms.DecimalField(label='Interest')
    penalty = forms.DecimalField(label='Penalty')
    adjustments = forms.DecimalField(label='Adjustments')
