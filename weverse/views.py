from django.shortcuts import render

# Create your views here.
def bts(request):
    return render(request, 'bighit.html')

def seventeen(request):
    return render(request, 'pledis.html')

def EXO(request):
    return render(request, 'SM.html')

def astro(request):
    return render(request, 'fantagio.html')