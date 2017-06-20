from django.shortcuts import render, HttpResponse

# Create your views here.

def ex00(request):
    return render(request, "ex00/index.html")
    
