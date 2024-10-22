from django.urls import path
from . import views

urlpatterns=[
    path('home',views.adminHomePage,name='admin_link'),
    path('login',views.adminLoginPage,name='adminlogin_link'),
    path('delete/<pk>',views.deleteFun,name='delete_link'),    #<pk> is a variable ie used to store the i.id value from delete btn
    path('edit',views.editFun,name='edit_link'),
    path('update',views.updateFun,name='update_link'),
    path('sellerapprovals',views.sellerapprovals,name='sellerapprovals'),
    path('processapproval',views.processApproval,name='processapproval'),


]