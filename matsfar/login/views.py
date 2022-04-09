from django.shortcuts import render 
from django.http import HttpResponse


# Create your views here.

def index(request):
    name = 'ayo'
    age = 25
    email = 'ayo@gmail.com'

    context = {
            'name':name,
            'age':age,
            'email':email,
    }

    return render(request,'index.html', context)



def sum(request):
 
    a = float(request.GET['a'])
    b = float(request.GET['b'])

    c = a + b

    return render(request, 'sum.html',{'res':c})    

