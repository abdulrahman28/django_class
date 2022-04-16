from django.shortcuts import render 
from django.http import HttpResponse
from .models import intel


# Create your views here.

def index(request):
    intel1 = intel()
    intel2 = intel()
    intel3 = intel()
    intel4 = intel()

    intel1.id = 1
    intel1.det = 'Your health is important to us'
    intel1.st = True

    intel2.id = 2
    intel2.det = 'Your life is precious to us'
    intel2.st = True

    intel3.id = 3
    intel3.det = 'You can never die in our clinic'
    intel3.st = False

    intel4.id = 4
    intel4.det = 'Outpatient Facility is Available'
    intel4.st = False

    context = {
        'intels' : [intel1,intel2,intel3,intel4],
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



      

