from django.shortcuts import render

# Create your views here.
def displayData(request):
    return render(request,'MyCssApp/index.html')