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
from django.urls import path, include
from base.views import home, room, room_form, main, update_room, delete_room, user_login, user_logout, delete_account, delete_message, register_page, user_profile, update_user, topics_page, activity_page, all_activities, follow_toggle, add_participant, search
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'base.views.custom_404_view'

urlpatterns = [
    path('nikoloz-admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/<str:q>/', search, name='search'),
    path('login-register/', user_login, name='login-register'),
    path('logout/', user_logout, name='logout'),
    path('delete-account/', delete_account, name='deleteacc'),
    path('register/', register_page, name='register'),
    path('room/<slug:slug>/', room, name='room'),
    path('create-room/', room_form, name='create-room' ),
    path('update-room/<int:pk>/', update_room, name='update-room'),
    path('delete-room/<int:pk>/', delete_room, name='delete-room'),
    path('delete-message/<int:pk>/', delete_message, name='delete-message'),
    path('profile/@<str:username>/', user_profile, name='user-profile'),
    path('update-user/', update_user, name='update-user'),
    path('topics/', topics_page, name='topics'),
    path('activity/', activity_page, name='activity'),
    path('all-activities/<int:pk>/', all_activities, name='allactivities'),
    path('follow-toggle/<int:pk>/', follow_toggle, name='follow-toggle'),
    path('add-participant/<int:pk>/', add_participant, name='add-participant'),


    # working different paths
    path('api/', include('base.api.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)