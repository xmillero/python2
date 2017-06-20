from django.shortcuts import render, HttpResponse

# Create your views here.

def ex01(request):
    return render(request, "ex01/django.html")
    return render(request, "ex01/affichage.html")
    return render(request, "ex01/templates.html")