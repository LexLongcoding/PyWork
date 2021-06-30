from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('travels', views.travels),
    path('addtrip', views.new),
    path('create', views.create),
    path('trip/<int:trip_id>/view', views.view),
    path('trip/<int:trip_id>/delete', views.delete),
    #path('<int:trip_id>/view', views.view),
    path('<int:trip_id>', views.index),
    path('trip/<int:id>/join', views.join_trip),
    path('trip/<int:id>/cancel', views.cancel_trip),
    #path('view/<int:id>', views.view)


]