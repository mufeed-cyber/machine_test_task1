from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from sellerapp.models import *

def index_funName(request):
    return render(request,'index.html')

def aboutPage(request):
    return render(request,'about.html')

def regForm(request):
    if request.method=='POST':
        name1=request.POST.get('nm')
        place1=request.POST.get('pl')
        email1=request.POST.get('em')
        pass1=request.POST.get('psw')
        age1=request.POST.get('age')

        ex=customertbl.objects.filter(email=email1)
        if ex:
            return render(request,'registration.html',{'error_reg':'Email Already Exists'})
        else:
            obj=customertbl.objects.create(
                name=name1,
                age=age1,
                place=place1,
                email=email1,
                password=pass1,
            )
            obj.save()

            if obj:
                return render(request,'login.html')
            else:
                return render(request,'registration.html')

    else:
        return render(request,'registration.html')

def loginPage(request):
    if request.method=='POST':
        email1=request.POST.get('em')
        pass1=request.POST.get('psw')
        userobjs=customertbl.objects.filter(email=email1,password=pass1)
        sellerobj=sellertbl.objects.filter(selleremail=email1,sellerpassword=pass1)
        if userobjs:
            for i in userobjs:
                # print(i.id)    #just for checking the checking the result come or not
                # print(i.name)

                request.session['user_id']=i.id
                # request.session['em1']=email1
                # request.session['ps1']=pass1
            return render(request,'index.html')
        elif sellerobj:
            for i in sellerobj:
                request.session['seller_id']=i.id
                print('inside seller')
            return redirect('/sellerapp')
        else:
            return render(request,'login.html',{"error_msg":"Invalid Email or Password"})  #dict for showing an error msg 

    return render(request,'login.html')


def logoutPage(request):
    if 'user_id' in request.session:
        del request.session['user_id']

        return render(request,'index.html')
    else:
        return render(request,'index.html')
    

def profilePage(request):

    obj=customertbl.objects.get(id=request.session['user_id'])
    return render(request,'user_profile.html',{"userid":obj})


def email(request):
    if request.method=="POST":
        nm=request.POST.get('nm')
        em=request.POST.get('em')
        msg=request.POST.get('msg')
        sub='Hello '+nm
        message='Thank you for your feedback'
        send_mail(sub,message,settings.EMAIL_HOST_USER,[em],fail_silently=False)
        messages.success(request,'Email sended successfully.')
        return redirect('/email')     

    else:
        return render(request,'email.html')


def viewallPage(request):
    objs=producttbl.objects.all
    return render(request,'viewall.html',{'data':objs})

def addtocart(request):
    userid=request.session['user_id']
    userobj=customertbl.objects.get(id=userid)
    proid=request.GET.get('idn')
    proobj=producttbl.objects.get(id=proid)
    cartitem,created=carttbl.objects.get_or_create(customer=userobj,product=proobj)
    if not created:
        cartitem.quantity+=1
        cartitem.save()
        messages.success(request,'Product added to cart')
        return redirect('/viewall')
    else:
        messages.success(request,'New Product added to cart')
        return redirect('/viewall')
    
def viewcart(request):
    userid=request.session['user_id']
    userobj=customertbl.objects.get(id=userid)
    cartobj=carttbl.objects.filter(customer=userobj)
    request.session['totalprice']=0
    request.session['totalquantity']=0
    for i in cartobj:
        request.session['totalprice']+=(i.product.cakeprice*i.quantity)
        request.session['totalquantity']+=(i.quantity)
    return render(request,'viewcart.html',{'cartobj':cartobj,'total':request.session['totalprice'],'quantity':request.session['totalquantity'],'username':userobj.name})

def addtowishlist(request):
    userid=request.session['user_id']
    userobj=customertbl.objects.get(id=userid)
    proid=request.GET.get('idn')
    proobj=producttbl.objects.get(id=proid)
    wishlistitem,created=wishlistbl.objects.get_or_create(customer=userobj,product=proobj)
    if not created:
        wishlistitem.save()
        messages.success(request,'Product added to wishlist')
        return redirect('/viewall')
    else:
        wishlistitem.save()
        messages.success(request,'Product Item added to wishlist')
        return redirect('/viewall')
    
def viewwishlist(request):
    userid=request.session['user_id']
    userobj=customertbl.objects.get(id=userid)
    wishlistobj=wishlistbl.objects.filter(customer=userobj)
    return render(request,'viewwishlist.html',{'wishlistobj':wishlistobj,'username':userobj.name})

# def buyone(request):
#     userid=request.session['user_id']
#     userobj=customertbl.objects.get(id=userid)
#     cartid=request.GET.get('cid')
#     if cartid:
#         cartobj=carttbl.objects.get(customer=userobj,id=cartid)
       
#     else:
#         proid=proid=request.GET.get('idn')
#         proobj=producttbl.objects.get(id=proid)
#         cartobj=carttbl.objects.create(
#             customer=userobj,
#             product=proobj
#         )
#         cartobj.save()

#     request.session['totalprice']=0
#     # for i in cartobjs:
#     request.session['totalprice']+=(cartobj.product.cakeprice*cartobj.quantity)
#     return render(request,'checkout.html',{'cartobj':cartobj,'userobj':userobj,'totalprice':request.session['totalprice']})
    
def deleteone(request):
    userid=request.session['user_id']
    userobj=customertbl.objects.get(id=userid)
    cartid=request.GET.get('cid')
    cartobj=carttbl.objects.get(customer=userobj,id=cartid)
    cartobj.delete()
    return redirect('/viewcart')

# def placeorder(request):
#     cartid=request.GET.get('cid')
#     cartobj=carttbl.objects.get(id=cartid)
#     proobj=cartobj.product
#     proobj.quantity-=cartobj.quantity
#     proobj.save()
#     cartobj.delete()
#     return redirect('/viewcart')