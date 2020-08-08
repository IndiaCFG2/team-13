from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

print(2)


def index(request):
    temp_dict = {'name': 'Anurag'}
    return render(request, "admin_app/index.html", temp_dict)
