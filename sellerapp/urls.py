from django.urls import path
from . import views

from django.conf.urls.static import static    #this 2 itmes are importing for assecing the uploaded files
from django.conf import settings


urlpatterns=[
    path('',views.sellerHomePage),
    path('registration',views.sellerRegPage,name='registration'),
    path('logout',views.sellerLogout,name='logout'),
    path('upload',views.uploadPage,name='upload'),
    path('myproducts',views.myproducts,name='myproducts'),
    path('editmyproducts',views.editmyproducts,name='editmyproducts'),
    path('deletemyproducts',views.deletemyproducts,name='deletemyproducts'),
    path('approval',views.approval,name='approval'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)