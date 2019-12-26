from django.http import HttpRequest
from datetime import datetime
from . import models


def get_context(request: HttpRequest) -> {str: str}:
    """
    helper function to retrieve user information from http request
    :param request:
        http request
    :return:
        a dictionary with username, source ip and user browser type
    """
    r = {'user': 'unknown', 'client_ip': 'unknown', 'browser_type': 'unknown'}

    if request.user:
        r['user'] = request.user.username
        if r['user'] in ['nurse001','nurse002','nurse003']:
            r['user_icon'] = r['user'] + '.jpg'
        else:
            r['user_icon'] = 'nurseX.png'
    if 'REMOTE_ADDR' in request.META:
        r['client_ip'] = request.META['REMOTE_ADDR']
    if 'HTTP_USER_AGENT' in request.META:
        r['browser_type'] =  request.META['HTTP_USER_AGENT']

    return r


def validate_data(data: {str: str}) -> [str]:
    """
    validate patient data from the form input
    :param data:
        a dictionary contains the patient data (as defined in patients.forms.PatientForm)
    :return:
        a list of error messages, the messages will be displayed in the frontend
    """
    r = []

    if 'first_name' in data:
        pass
    if 'last_name' in data:
        pass
    if 'gender' in data:
        pass
    if 'birth' in data:
        try:
            date = datetime.strptime(data['birth'], '%Y-%m-%d')
        except ValueError:
            r.append('bad date: must be in the format of yyyy-mm-dd')
    if 'phone_number' in data:
        pass
    if 'weight' in data:
        try:
            fp = float(data['weight'])
            if fp < 0.0 or fp > 1000.0:
                r.append('bad weight: weight must be between 0 and 1000 kg')
        except ValueError:
            r.append('bad weight: weight must be a number')
    if 'height' in data:
        try:
            fp = float(data['height'])
            if fp < 0.0 or fp > 300.0:
                r.append('bad height: height must be between 0 and 300 cm')
        except ValueError:
            r.append('bad height: height must be a number')
    if 'study_nurse_name' in data:
        pass

    return r


def save_patient_data(data: {str: str}, username: str) -> bool:
    """
    save patient data to database
    :param data:
        a dictionary contains patient data, as defined in patients.models.Patient
    :param username:
        the username of the study nurse
    :return:
        true if saved successfully
    """
    r = True

    try:
        date = datetime.strptime(data['birth'], '%Y-%m-%d')
        patient = models.Patient(
            first_name=data['first_name'],
            last_name=data['last_name'],
            gender=data['gender'],
            birth=date,
            phone_number=data['phone_number'],
            height=data['height'],
            weight=data['weight'],
            study_nurse_name=username
        )
        patient.save()
    except ValueError:
        r = False

    return r
