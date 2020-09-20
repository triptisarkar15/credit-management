from django.urls import path
from. import views

urlpatterns=[
    path('',views.home,name='home'),
    path('users', views.userinfo, name='users'),
    
    path('users/details/<int:pk>', views.UserDetail.as_view(), name='details'),
    path('transactions/<int:pk>', views.Transaction.as_view(), name='transactions'),
    
    
]

