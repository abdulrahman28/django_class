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

    a = request.POST['first']
    b = request.POST['second']

    if a == '' or b == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'sum.html', context)  

    else:
        a = float(a)
        b = float(b)       
        c = 'The result is ' + str(a + b)
        context = {
            'res':c
            }
        return render(request, 'sum.html', context)



      

