from django.urls import path
from . import views

urlpatterns=[
    path('',views.index_funName,name='index_link'),
    path('about/',views.aboutPage,name='about_link'),
    path('register',views.regForm,name='regName_for_link'),
    path('login',views.loginPage,name='login_link'),
    path('logout',views.logoutPage,name='logout_link'),
    path('profile',views.profilePage,name='userprofile_link'),
    path('email',views.email,name='email'),
    path('viewall',views.viewallPage,name='viewall'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('addtowishlist',views.addtowishlist,name='addtowishlist'),
    path('viewwishlist',views.viewwishlist,name='viewwishlist'),
    path('deleteone',views.deleteone,name='deleteone'),


]