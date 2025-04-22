from django.shortcuts import render
from django.contrib.auth.decorators import (
    login_required,
)  # to protect function-based views

# Create your views here.


# keep protected
@login_required
def about(request):
    return render(request, "about/about.html")
