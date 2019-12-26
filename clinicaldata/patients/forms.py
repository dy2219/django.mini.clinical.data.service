from django import forms
import datetime


class PatientForm(forms.Form):
    first_name = forms.CharField(label='First Name',  max_length=32)
    last_name = forms.CharField(label='Last Name', max_length=32)
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female')])
    birth = forms.DateField(label='Date of Birth (yyyy-mm-dd)', input_formats=['%Y-%m-%d'])
    phone_number = forms.CharField(label='Phone Number', max_length=16)
    height = forms.FloatField(label='Height (cm)')
    weight = forms.FloatField(label='Weight (kg)')
