"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
