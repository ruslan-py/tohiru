from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'index.html')

def reversed(request):
    ustext = request.GET['us_text']
    len_words = len(ustext.split())
    rev_text = ustext[::-1]
    return render(request, 'reversed.html', {'us_text': rev_text, "lenwords": len_words})