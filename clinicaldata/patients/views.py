from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms
from . import services
from . import models


@login_required(login_url='/accounts/login')
def home(request) -> HttpResponse:
    context = services.get_context(request)
    return render(request, 'index.html', context)


@login_required(login_url='/accounts/login')
def view_data(request) -> HttpResponse:
    context = services.get_context(request)

    patient_list = models.Patient.objects.all()
    context['patient_list'] = patient_list

    return render(request, 'view_data.html', context)


@login_required(login_url='/accounts/login')
def add_data(request) -> HttpResponse:
    context = services.get_context(request)

    if request.method == 'POST':
        data = request.POST
        err = services.validate_data(data)
        if err:
            context['state'] = "ERROR"
            context['error_message'] = err
        elif services.save_patient_data(data, request.user.username):
            context['state'] = "SUCCESS"
        else:
            context['state'] = "ERROR"
            context['error_message'] = ['Failed to save patient data, unknown error.']
    else:
        context['state'] = "NEW"
        context['form'] = forms.PatientForm()

    return render(request, 'add_data.html', context)

