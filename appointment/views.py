from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from .models import *
def myview(request):
    appointments_by_date=Appointments.objects.order_by("time")
    context={"appointments_by_date":appointments_by_date}
    return render(request,"appointment/htmlfile.html",context)
def show_user_appointments(request,user_id):
    try:
        user=Person.objects.get(pk=user_id)
        all=user.appointments_set.all()
        context={'all':all}
    except Person.DoesNotExist:
       raise Http404("No such user")
    return render(request,"appointment/show.html",context)
def all_appointments(request):
    all=Appointments.objects.order_by("time")
    result=", ".join([str(a.time) for a in all])
    return HttpResponse(result)

# Create your views here.
