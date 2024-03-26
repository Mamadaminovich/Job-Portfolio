from django.shortcuts import render

from .models import *

def home(context):
    return render(context, "index.html", {})