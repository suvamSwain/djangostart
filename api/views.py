from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(Request):
    return HttpResponse("<h1>Here is the code</h1>")