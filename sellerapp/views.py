from django.shortcuts import render,redirect
from . models import *
from userapp.models import *
from userapp.views import *


def sellerHomePage(request):
    sellerid=request.session['seller_id']
    sellerobj=sellertbl.objects.get(id=sellerid)
    return render(request,'sellerhomepage.html',{'approvalstatus':sellerobj.approval})

def sellerLogout(request):
    if 'seller_id' in request.session:
        del request.session['seller_id']
        return render(request,'login.html')
    
def sellerRegPage(request):
    if request.method=='POST':
        nm=request.POST.get('nm')
        age=request.POST.get('age')
        ph=request.POST.get('ph')
        em=request.POST.get('em')
        psw=request.POST.get('psw')
        obj=sellertbl.objects.filter(selleremail=em)
        if obj:
            return render(request,'seller_reg_page.html',{'seller_reg_email_error':'Alreay exists'})
        else:
            newsellerobj=sellertbl.objects.create(
                sellername=nm,
                sellerage=age,
                sellerphone=ph,
                selleremail=em,
                sellerpassword=psw
            )
            newsellerobj.save()
            return render(request,'sellerhomepage.html')
    else:    
        return render(request,'seller_reg_page.html')

def uploadPage(request):
    if request.method=='POST':
        cname=request.POST.get('cn')
        cprice=request.POST.get('cp')
        ccatgory=request.POST.get('category')
        cimg=request.FILES.get('ci')
        cqty=request.POST.get('cqty')

        sellerid=request.session['seller_id']
        sellerobj=sellertbl.objects.get(id=sellerid)

        obj=producttbl.objects.create(
            cakename=cname,
            cakeprice=cprice,
            category=ccatgory,
            cakeimage=cimg,
            quantity=cqty,
            selleridFK=sellerobj
        )
        print('cakeprice',cprice,type(cprice)),
        obj.save()
        if obj:
            return render(request,'upload.html',{'upload_msg':'Product uploaded successfully '})
        else:
            return render(request,'upload.html',{'upload_msg':'Product failed to upload'})
    return render(request,'upload.html')

def myproducts(request):
    sellerid=request.session['seller_id']
    sellerobjs=sellertbl.objects.get(id=sellerid)
    proobjs=producttbl.objects.filter(selleridFK=sellerobjs)
    return render(request,'myproducts.html',{'proobjs':proobjs})

def editmyproducts(request):
    proid=request.GET.get('proid')
    proobjs=producttbl.objects.filter(id=proid)
    if request.method=='POST':
        cname=request.POST.get('cn')
        cprice=request.POST.get('cp')
        cqty=request.POST.get('cqty')
        ccatgory=request.POST.get('category')
        cimg=request.FILES.get('ci')
        for i in proobjs:
            i.cakename=cname
            i.cakeprice=cprice
            i.quantity=cqty
            i.category=ccatgory
            if cimg:
                i.cakeimage=cimg
            i.save()
        return render(request,'editmyproducts.html',{'proobjs':proobjs,'upload_msg': 'Product updated successfully'})

    else:   
        return render(request,'editmyproducts.html',{'proobjs':proobjs})

def deletemyproducts(request):
    proid=request.GET.get('proid')
    proobjs=producttbl.objects.filter(id=proid)
    proobjs.delete()
    return redirect('/sellerapp/myproducts')

