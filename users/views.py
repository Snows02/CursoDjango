"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from posts.models import Profile

# Exceptions
from django.db.utils import IntegrityError


def login_view(request):
    """Login view:"""
    # Estoy esperando recibir los datos por un metodos POST para autenticarlos
    # Una vez autenticados genero la sesion y redirijo a un nuevo template
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Genera la sesion
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid username or password'
            })
    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {
                'error': 'Password confirmation does not match'
            })
        try:
            user = User.objects.create_user(
                username=username, password=password
            )
        except IntegrityError:
            return render(request, 'users/signup.html', {
                'error': 'Username is alredy in user'
            })
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
