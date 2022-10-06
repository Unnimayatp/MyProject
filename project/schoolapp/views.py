from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import json
from schoolapp.models import Person, get_cs_strings, get_b_strings
from .forms import PersonForm


from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):

    return render(request,'index.html',)


def personform_page(request):
    context = {}

    personform = PersonForm()
    context['personform'] = personform

    cs_strings = get_cs_strings()
    b_strings = get_b_strings()

    json_cs_strings = json.dumps(cs_strings)
    json_b_strings = json.dumps(b_strings)

    context['json_cs_strings'] = json_cs_strings
    context['json_b_strings'] = json_b_strings

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        gender = request.POST.get('gender', '')
        dateofbirth = request.POST.get('dateofbirth', '')
        phone_number = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        job = request.POST.get('job', '')
        purpose = request.POST.get('purpose', '')

        Form = Person(first_name=first_name, last_name=last_name, gender=gender, dateofbirth=dateofbirth,
                    phone_number=phone_number,
                    email=email, subject=subject, job=job, purpose=purpose)
        Form.save()

    return render(request, 'personform_page.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
