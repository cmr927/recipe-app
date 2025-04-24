from django.shortcuts import render
import logging

# Create your views here.


def home(request):
    logging.error("TEST TEST TEST")
    logging.error("TEST TEST TEST")
    logging.error("TEST TEST TEST")
    logging.error("TEST TEST TEST")
    logging.error("TEST TEST TEST")
    logging.error("TEST TEST TEST")
    return render(request, "home/home.html")
