from django.shortcuts import render

# Create your views here.
def show_geomap(request):
    return render(request, "geomap.html")