
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from todolist.models import task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    list_todolist = task.objects.filter(user=request.user)
    context = {
        'list_of_task': list_todolist,
    }

    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        description_show = request.POST.get('deskripsi')
        title_show = request.POST.get('judul')
        add_task =  task(
            user = request.user,
            title = title_show,
            description = description_show,
        )
        add_task.save()
        return redirect('todolist:show_todolist')        
    return render(request, 'create_task.html')

@login_required(login_url='/todolist/login/')
def delete(request, name):
    get_todolist =  task.objects.get(user=request.user, title=name)
    get_todolist.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def update(request, name):
    get_todolist =  task.objects.get(user=request.user, title=name)
    get_todolist.status = True
    get_todolist.save()
    return redirect('todolist:show_todolist')

