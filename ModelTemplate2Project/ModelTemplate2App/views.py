from django.http import JsonResponse
from django.shortcuts import render
from ModelTemplate2App.models import Classical_Dance_Forms,Modern_Dance
# from ModelTemplate2App.models import Modern_Dance
# Create your views here.
def display(request):
    cdancelist=Classical_Dance_Forms.objects.all()
    mdancelist=Modern_Dance.objects.all()
    # cdict={'cdancelist':cdancelist}
    dict={"cdancelist":cdancelist,"mdancelist":mdancelist}
    return render(request,'ModelTemplate2App/dance.html',context=dict)
# def display2(request):
#     mdancelist=Modern_Dance.objects.all()
#     mdict={'mdancelist':mdancelist}
#     return render(request,'ModelTemplate2App/dance.html',context=mdict)