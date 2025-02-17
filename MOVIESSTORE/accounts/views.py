from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from datetime import datetime
=======
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ForgotPasswordForm
from .models import UserProfile
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordResetForm
>>>>>>> 4b0cd93f860938d21c1efdb129804d2f57d8eeb3

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies.index')

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
<<<<<<< HEAD
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
=======
            auth_login(request, user)
            return redirect('movies.index')
>>>>>>> 4b0cd93f860938d21c1efdb129804d2f57d8eeb3

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
<<<<<<< HEAD
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html', {'template_data': template_data})
=======
    
    # Retrieve all orders for the logged-in user
    user_orders = request.user.order_set.all().order_by('id')

    # Add a user-specific order number instead of using the database ID
    for index, order in enumerate(user_orders, start=1):
        order.user_order_number = index  # Assign sequential numbers per user

    template_data['orders'] = user_orders
    return render(request, 'accounts/orders.html', {'template_data' : template_data})

def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            birthdate = form.cleaned_data["birthdate"]

            try:
                user = User.objects.get(username=username)
                profile = UserProfile.objects.get(user=user)

                if profile.birthdate == birthdate:
                    # Store user ID in session for password reset
                    request.session['reset_user_id'] = user.id
                    return redirect('accounts.reset_password')  # Redirect to reset password page
                else:
                    messages.error(request, "Incorrect birthdate.")
            except (User.DoesNotExist, UserProfile.DoesNotExist):
                messages.error(request, "User not found.")
    else:
        form = ForgotPasswordForm()

    return render(request, "accounts/forgot_password.html", {"form": form})

def reset_password(request):
    user_id = request.session.get("reset_user_id")
    if not user_id:
        messages.error(request, "Your session has expired. Please try the forgot password process again.")
        return redirect("accounts.forgot_password")

    user = User.objects.get(id=user_id)

    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']

            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)  # Keeps the user logged in
                messages.success(request, "Your password has been reset successfully.")
                del request.session['reset_user_id']  # Clear session
                return redirect("accounts.login")
            else:
                messages.error(request, "Passwords do not match.")
    else:
        form = PasswordResetForm()

    return render(request, "accounts/reset_password.html", {"form": form})
>>>>>>> 4b0cd93f860938d21c1efdb129804d2f57d8eeb3
