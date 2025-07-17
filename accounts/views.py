from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup_view(request):
    from .utils import is_valid_email, get_emails, get_active_usernames
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Validar email con función pura
            if is_valid_email(user.email):
                login(request, user)
                # Ejemplo de uso de funciones funcionales compuestas
                from django.contrib.auth import get_user_model
                User = get_user_model()
                all_users = User.objects.all()
                emails = get_emails(all_users)
                active_usernames = get_active_usernames(all_users)
                # Puedes usar emails y active_usernames para lógica adicional, logs, etc.
                messages.success(request, '¡Registro exitoso!')
                return redirect('profile')
            else:
                messages.error(request, 'Email inválido.')
        else:
            messages.error(request, 'Error en el registro. Por favor, inténtalo de nuevo.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirige al perfil después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al inicio de sesión después de cerrar sesión

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
