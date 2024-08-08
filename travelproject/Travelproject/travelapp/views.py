from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,'index.html')
def more(request):
    return render(request,'generic.html')
def thanks(request):
    return render(request,'thanks.html')