from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            task = request.POST.get('task')
            new_todo = todo(user=request.user, todo_name=task)
            new_todo.save()
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }    
    return render(request,'todop/home.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            return redirect('home')
    
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            validate_user = authenticate(username=username, password=password)
            if validate_user is not None:
                login(request, validate_user)
                return redirect('home')
            else:
                return redirect('login')

    return render(request,'todop/login.html',{})
def addtask(request):
    pass
def LogoutView(request):
    logout(request)
    return redirect('login')
@login_required
def DeleteTask(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home')

@login_required
def Update(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home')
