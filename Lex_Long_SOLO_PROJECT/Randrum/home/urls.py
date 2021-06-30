from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('generate', views.generate),
    path('new', views.new),
    path('kit/<int:kit_id>/view_kit', views.view_kit),
    path('profile/<int:id>', views.profile),
    path('kit/<int:id>/add_favorite', views.add_favorite),
    path('kit/<int:kit_id>/delete', views.delete),
    path('kit', views.kit), # temporary route to see kit page

    
]