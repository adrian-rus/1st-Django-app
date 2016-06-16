# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    day = datetime.date.today()
    return render(request, "sitepages/home.html",
                  {"welcome_variable": "Welcome home, Coder!",
                   "day": day})


def contact(request):
    return render(request, "sitepages/contact.html",
                  {"name": "Adrian Rus",
                   "phone_no": "08******56",
                   "email": "adrian.rus@live.com"})


def about(request):
    return render(request, "sitepages/about.html", {"about": "This is the first Django app I have built. It is a "
                                                             "simple"
                                                             " app with a base menu and 3 views (home, contact and "
                                                             "about)"
                                                             " I have used Bootstrap for responsiveness and to add"
                                                             " a bit of colour. "})


