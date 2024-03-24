from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('delete-task/<str:name>/', views.DeleteTask, name='delete'),
    path('update/<str:name>/', views.Update, name='update'),
    path('accounts/login/',views.loginpage, name='login'),
]