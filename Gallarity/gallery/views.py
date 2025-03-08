from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import logging
from .models import Wallpaper


logger = logging.getLogger(__name__)

# Store uploaded files in a temporary list for demonstration
uploaded_files = []

# Index View
def index(request):
    print("Displaying uploaded files:", uploaded_files)
    # Pass the uploaded files and wallpapers to the template
    wallpapers = Wallpaper.objects.all()  # Retrieve wallpapers from the database
    return render(request, 'index.html', {
        'uploaded_files': uploaded_files,
        'wallpapers': wallpapers,
        'MEDIA_URL': settings.MEDIA_URL,
    })

# Upload View
def upload(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        profile_dp = request.FILES.get('profile_dp')
        file_upload = request.FILES.get('file_upload')

        if username and profile_dp and file_upload:
            # Save files using FileSystemStorage
            fs = FileSystemStorage()
            profile_dp_name = fs.save(profile_dp.name, profile_dp)
            file_upload_name = fs.save(file_upload.name, file_upload)

            # Append uploaded file details to the temporary list
            uploaded_files.append({
                'username': username,
                'profile_dp': fs.url(profile_dp_name),
                'file_upload': fs.url(file_upload_name),
            })

            # Debugging Output
            print("Form submitted:")
            print("Username:", username)
            print("Profile Picture URL:", fs.url(profile_dp_name))
            print("Uploaded File URL:", fs.url(file_upload_name))

            # Redirect to the index page
            return redirect('index')
        else:
            # Handle missing fields
            return render(request, 'upload.html', {'error': 'Please upload all files!'})

    return render(request, 'upload.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.profile_picture = form.cleaned_data['profile_dp'] # type: ignore
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('signin')
    return render(request, 'signup.html')

# Signin View
def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'signin.html')

# Search Wallpapers View
def search_wallpapers(request):
    query = request.GET.get('q', '')
    wallpapers = Wallpaper.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'wallpapers': wallpapers, 'query': query})

def settings_view(request):
    return render(request, 'setting.html')

def about_view(request):
    return render(request, 'about.html')

def terms_view(request):
    return render(request, 'terms.html')
