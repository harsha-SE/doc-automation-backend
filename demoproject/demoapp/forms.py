from django import forms

class UserForm(forms.Form):
    client = forms.CharField()
    company_desc = forms.CharField()
    directors = forms.CharField()
    independent = forms.CharField()
    no_of_meetings = forms.IntegerField()
    reporting_year = forms.IntegerField()
    budget = forms.FloatField()
    team_responsibility = forms.CharField()
    management_reporting_line = forms.CharField()
    export_format = forms.ChoiceField()
