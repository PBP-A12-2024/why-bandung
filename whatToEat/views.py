from django.shortcuts import render

# Create your views here.
def show_slider(request):
    return render(request, 'whatToEat.html')
