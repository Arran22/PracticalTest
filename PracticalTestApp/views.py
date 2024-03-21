from django.shortcuts import render

from django.http import HttpResponse
from PracticalTestApp.models import People, Cat

def home(request):
    context_dict = {}
    context_dict['peoples'] = People.objects.order_by('last_name')
    return render(request, 'Practical/home.html', context=context_dict)

def about(request):
    context_dict = {}
    context_dict['cats'] = Cat.objects.order_by('cat_name')
    return render(request, 'Practical/about.html', context=context_dict)
    