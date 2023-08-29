from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from  .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'app_auth/profile.html')
    user_form = RegistrationForm()
    return render(request, 'app_auth/register.html', {'user_form': user_form})


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error', 'Пользователь не найден'})

def logout_view(requset):
    logout(requset)
    return redirect(reverse('login'))
