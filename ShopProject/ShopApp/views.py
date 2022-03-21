from django.shortcuts import render

# Create your views here.
def tees(request):
    dict={'heading':'T-Shirt Page',
    'link':'https://www.amazon.in/b/ref=spb_gw_may4?node=21251246031&pf_rd_r=Y0BJ47J6JXSB85HTZGS5&pf_rd_p=099c4527-7018-4062-b1b1-242baca39f5e&pd_rd_r=f5b19df1-cbae-49c2-b8e4-c8618c6802f0&pd_rd_w=8x42q&pd_rd_wg=GsCx7&ref_=pd_gw_unk'}
    return render(request,'ShopApp/details.html',context=dict)
def shoes(request):
    dict={'heading':'Shoes Page',
    'link':'https://www.libertyshoesonline.com/'}
    return render(request,'ShopApp/details.html',context=dict)
def index(request):
    return render(request,'ShopApp/index.html')