from django.shortcuts import render

# Create your views here.
def costa(request):
    return render (request, 'costa.html')
def felipe(request):
    return render (request, 'felipe.html')