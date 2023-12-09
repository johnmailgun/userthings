from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm, ProfilePic
from pestpoge.models import Post
# Create your views here.
def accounts_index(request):
    return render(request, 'userthings/index_3.html')

def user_register(request):
    if request.method == "POST":
        username1 = request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return render(request, 'somethingerror.html')
        else:
            User.objects.create_user(username1,email1,password1)
            return render(request, 'index.html')
    else:
        context = {'form':RegisterForm()}
        return render(request, 'userthings/user_register.html', context)
    
def user_login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password1']
    
        user = authenticate(username=username1,password=password1)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'somethingerror.html')
    else:
        context = {'form':LoginForm()}
        return render(request, 'userthings/user_login.html', context)
    
def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def user_profile(request):
    user = authenticate(request.user)
    if request.user.is_authenticated:
        mymodel = Post.objects.filter(author=request.user)
        context = {'mymodel':mymodel, 'form':ProfilePic()}
        return render(request,'userthings/user_profile.html', context)
    else:
        return render(request,'userthings/user_profile.html')