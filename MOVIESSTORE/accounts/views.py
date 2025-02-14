from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from datetime import datetime

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    show_forgot_password = False

    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data, 'show_forgot_password': show_forgot_password})
    elif request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                template_data['error'] = 'The username or password is incorrect.'
                show_forgot_password = True
                return render(request, 'accounts/login.html', {'template_data': template_data, 'show_forgot_password': show_forgot_password})
            else:
                auth_login(request, user)
                return redirect('home.index')
        else:
            template_data['error'] = 'Please enter both username and password.'
            return render(request, 'accounts/login.html', {'template_data': template_data, 'show_forgot_password': show_forgot_password})

def forgot_password(request):
    template_data = {}
    template_data['title'] = 'Forgot Password'

    if request.method == 'POST':
        if 'forgot_password' in request.POST:
            username = request.POST.get('username')
            birthdate = request.POST.get('birthdate')
            try:
                birthdate = datetime.strptime(birthdate, '%m-%d-%Y').date()
                user = CustomUser.objects.get(username=username, birthdate=birthdate)
                template_data['username'] = username
                template_data['birthdate'] = birthdate.strftime('%m-%d-%Y')
                template_data['show_reset_password'] = True
            except CustomUser.DoesNotExist:
                template_data['error'] = 'The username or birthdate is incorrect.'
            except ValueError:
                template_data['error'] = 'Invalid birthdate format. Please use MM-DD-YYYY.'
            return render(request, 'accounts/forgot_password.html', {'template_data': template_data})
        elif 'reset_password' in request.POST:
            username = request.POST.get('username')
            birthdate = request.POST.get('birthdate')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                template_data['error'] = 'Passwords do not match.'
                template_data['username'] = username
                template_data['birthdate'] = birthdate
                template_data['show_reset_password'] = True
            else:
                try:
                    validate_password(new_password)
                    user = CustomUser.objects.get(username=username, birthdate=datetime.strptime(birthdate, '%m-%d-%Y').date())
                    user.set_password(new_password)
                    user.save()
                    return redirect('accounts.login')
                except ValidationError as e:
                    template_data['error'] = e.messages
                except CustomUser.DoesNotExist:
                    template_data['error'] = 'The username or birthdate is incorrect.'
            return render(request, 'accounts/forgot_password.html', {'template_data': template_data})
    else:
        return render(request, 'accounts/forgot_password.html', {'template_data': template_data})

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            user.birthdate = form.cleaned_data.get('birthdate')
            user.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html', {'template_data': template_data})