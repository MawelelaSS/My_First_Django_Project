from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    print(request.method)  # Print the request method (GET or POST)
    
    if request.method == 'POST':
        print('-------- Inside POST request --------')  # To check if it's POST
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(f"First Name: {first_name}, Last Name: {last_name}, Username: {username}, Email: {email}")  # Print form data
        
        if password1 == password2:
            print('Passwords match')  # Confirm passwords match
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                print('Username taken')  # Print if username is already taken
                messages.info(request, 'Username is already taken.')
                return redirect('register')  # Redirect back to the registration page
            
            # Check if the email already exists
            elif User.objects.filter(email=email).exists():
                print('Email taken')  # Print if email is already taken
                messages.info(request, 'Email is already taken.')
                return redirect('register')  # Redirect back to the registration page
            
            else:
                # Create the user if everything is valid
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                print('User created successfully')  # Print user creation success
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')  # Redirect to home or login page after successful registration
        else:
            print('Passwords do not match')  # Print if passwords do not match
            messages.info(request, "Passwords do not match.")
            return redirect('register')  # Redirect back if passwords don't match
    
    else:
        print('-------- Inside GET request --------')  # To check if it's a GET request
        # If it's a GET request, render the registration page
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
            
    else:
        return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')