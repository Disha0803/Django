from django.shortcuts import render

# Create your views here.
def movieNews(request):
    dict={'heading':'Movie News',
    'news1':'IPL',
    'news2':'Rohit Sharma',
    'news3':'India'}
    return render(request,'blogApp/news.html',context=dict)
def cricketNews(request):
    dict={'heading':'Cricket News',
    'news1':'IPL',
    'news2':'Rohit Sharma',
    'news3':'India'}
    return render(request,'blogApp/news.html',context=dict)
def educationNews(request):
    dict={'heading':'Education News',
    'news1':'IPL',
    'news2':'Rohit Sharma',
    'news3':'India'}
    return render(request,'blogApp/news.html',context=dict)
def index(request):
    return render(request,'blogApp/index.html')