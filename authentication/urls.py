from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('signin',views.signin,name="signin"),
   path('signout',views.signout,name="signout"),
   path('signup',views.signup,name="signup"),
   path('showadmin',views.showadmin,name="showadmin"),
   path('delete/<int:id>/',views.delete,name="delete"),
   path('<int:id>/',views.update,name="update"),
   
   
  
   
]
