from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    #path('success', views.success),
    path('wall', views.wall),
    path('new_post', views.new_post),
    path('add_comment/<int:id>', views.new_comment),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.delete_comment),
    #path('edit/<int:id>', views.edit)
]