from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('update/<int:id>', views.update),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('addwish', views.new),
    path('create', views.create),
    path('grant/<int:id>', views.grant_wish),
    path('wish/<int:wish_id>/edit', views.edit),
    path('wish/<int:wish_id>/delete', views.delete),
    
    
    

]