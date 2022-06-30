from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def callName(request):
    return HttpResponse ("Hello welcome to DJango")


def firstENV(request):
    return render(request, 'firstENV.html')


def callLink(request):
    return render(request, 'linkFile.html')

def callNewPage(request):
    return render(request,'new_page.html')