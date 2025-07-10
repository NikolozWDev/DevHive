from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic, Message, User
from .form import RoomForm, UserForm, MyUserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def main(request):
    context = {}
    return render(request, 'main.html', context)


def user_login(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist')
    context = {'page': page}
    return render(request, 'login-register.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def register_page(request):
    messages.error(request, "sorry, registration is now closed.")
    return redirect('login-register')

def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')
    context = {}
    return render(request, 'delete-account.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()[0:4]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))[:3]
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'q':q, 'room_messages': room_messages}
    return render(request, 'home.html', context)

def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()[:3]
    topics = Topic.objects.all()[0:4]
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'profile.html', context)

@login_required(login_url='login-register')
def update_user(request):
    form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=request.user.id)
    context = {'form': form}
    return render(request, 'update-user.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = Message.objects.create(
                user = request.user,
                room = room,
                body = request.POST.get('body')
            )
            room.participants.add(request.user)
            return redirect('room', pk=room.id)
        else:
            return redirect('login-register')
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'room.html', context)

@login_required(login_url='login-register')
def room_form(request):
    form = RoomForm()
    topics = Topic.objects.all()[0:4]
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, 'room_form.html', context)

@login_required(login_url='login-register')
def update_room(request, pk):
    topics = Topic.objects.all()[0:4]
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('you are not owner of this room!')
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'room_form.html', context)

@login_required(login_url='login-register')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('you are not owner of this room!')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'room': room}
    return render(request, 'delete_room.html', context)

def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('you are not owenr of this message!')
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context = {'message': message}
    return render(request, 'delete-message.html', context)

def topics_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def activity_page(request):
    room_messages = Message.objects.all()
    context = {'room_messages': room_messages}
    return render(request, 'activity.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', {
        'user': request.user
    }, status=404)