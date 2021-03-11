from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('abc/',views.abc),
    path('accounts/da.html/',views.cont),
    path('acb/',views.acb),
    path('login/',views.login),
  
    path('login/<str:pk1>/',views.bd),
    path('ach/<str:pk3>/',views.ach),
    path('rm/<str:pk4>/',views.rm ),

    path('sam/',views.sam)
]

