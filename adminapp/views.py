from django.shortcuts import render,redirect
from userapp.models import customertbl
from sellerapp.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def adminHomePage(request):
    obj=customertbl.objects.all
    return render(request,'adminhomepage.html',{"allusers":obj})

def adminLoginPage(request):
    return render(request,'admin_login_page.html')

def deleteFun(request,pk):
    obj=customertbl.objects.get(id=pk)
    obj.delete()
    return redirect('/adminapp/home')

def editFun(request):
    idvalue=request.GET.get('idn')
    obj=customertbl.objects.filter(id=idvalue)
    return render(request,'admin_edit.html',{"editobj":obj})

def updateFun(request):
    if request.method=='POST':
        idv=request.POST.get('idvalue')
        name1=request.POST.get('nm')
        place1=request.POST.get('pl')
        email1=request.POST.get('em')
        pass1=request.POST.get('psw')
        age1=request.POST.get('ag')
        obj=customertbl.objects.get(id=idv)
        
        obj.name=name1
        obj.age=age1
        obj.place=place1
        obj.email=email1
        obj.password=pass1
        obj.save()
        return redirect('/adminapp/home')
    
def sellerapprovals(request):
    sellerobjs=sellertbl.objects.all
    return render(request,'processapprovals.html',{'sellerobjs':sellerobjs})

def processApproval(request):
    sellerid=request.GET.get('sid')
    sellerobj=sellertbl.objects.get(id=sellerid)
    email=sellerobj.selleremail
    if sellerobj.approval==False:
        sellerobj.approval=True
        # message="Hi "+sellerobj.sellername+", Admin has Approved..."
        # send_mail('Mail From Admin',message,settings.EMAIL_HOST_USER,[sellerobj.selleremail],fail_silently=False)
        messages.success(request,'Email sended successfully')
    else:
        sellerobj.approval=False
        # message="Hi "+sellerobj.sellername+", Admin has removed your approval..."
        # send_mail('Mail From Admin',message,settings.EMAIL_HOST_USER,[sellerobj.selleremail],fail_silently=False)
        messages.success(request,'Email sended successfully')
    sellerobj.save()
    return redirect('/adminapp/sellerapprovals')
