from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import os

from .models import Person, DoorEvent


def index(request):
    people = Person.objects.all()
    files = os.listdir('media/')
    if not files:
        return HttpResponse('no data')
    file = files[0]
    context = {'file': file, 'people': people}
    return render(request, 'validation/index.html', context)


def validate(request):
    try:
        action_in = request.POST['action']
        file_name = request.POST['file_name']
        date_time_in = datetime.fromisoformat(file_name.strip('.gif'))
        person_in = Person.objects.filter(name=request.POST['choice']).first()
        DoorEvent(
                date_time=date_time_in, whos_there=person_in,
                action=action_in).save()
        os.rename('media/' + file_name, 'archive/' + file_name)
        return redirect('/validation/')
    except:
        return HttpResponse('something went wrong')


def new_user(request):
    new_name = request.POST['new_person']
    Person(name=new_name).save()
    return redirect('/validation/')
