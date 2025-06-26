"""
URL configuration for firstpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home, room, room_form, main, update_room, delete_room, user_login, user_logout, delete_account, delete_message, register_page, user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login-register/', user_login, name='login-register'),
    path('logout/', user_logout, name='logout'),
    path('delete-account/', delete_account, name='deleteacc'),
    path('register/', register_page, name='register'),
    path('room/<int:pk>/', room, name='room'),
    path('create-room/', room_form, name='create-room' ),
    path('update-room/<int:pk>/', update_room, name='update-room'),
    path('delete-room/<int:pk>/', delete_room, name='delete-room'),
    path('delete-message/<int:pk>/', delete_message, name='delete-message'),
    path('user-profile/<int:pk>', user_profile, name='user-profile'),
]