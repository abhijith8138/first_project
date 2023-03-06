from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return HttpResponse('hi abhijith')

def hello(request):
    return HttpResponse('<h1><button>hi abhijith<button></h1>')


def abhi(request):
    return HttpResponse('<h1>hai hello abhijith</h1>')