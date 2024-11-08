from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_page(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Logged in successfully.')
      return redirect('home')
    else :
      messages.error(request, 'Invalid username or password.')
      return redirect('login')
  return render(request, 'authentication/login.html')

def registration(request):
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()

      # Get the username and password from the form data
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')  # Or 'password' depending on your form's field

      # Authenticate and log the user in right after registration
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, 'Account created and logged in successfully.')
        return redirect("home")
  else:
    form = RegisterUserForm()

  return render(request, 'authentication/registration.html', {'form' : form })

def logout_user(request):
  logout(request)
  return redirect('login')
