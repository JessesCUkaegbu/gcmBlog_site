from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages 
from . models import *
from django.http import JsonResponse
# Create your views here.



def home(request):
    sliders = home_hero.objects.all()
    politics = PoliticsBlog.objects.all()[:4]
    technology = TechnologyBlog.objects.all()[:4]
    business = BusinessBlog.objects.all()[:4]
    sports = SportsBlog.objects.all()[:4]
    science = ScienceBlog.objects.all()[:4]
    featurevideo = featureVideo.objects.all()
    categories = BlogCategory.objects.all()[:2]
    context = {
        'sliders':sliders,
        'politics':politics,
        'technology':technology,
        'business':business,
        'sports':sports,
        'science':science,
        'featurevideo':featurevideo,
        'categories':categories,
    }
    return render(request, 'index.html', context)


def category_list(request):
    categories = BlogCategory.objects.all()
    blog_posts = Blog.objects.all()
    paginator = Paginator(blog_posts, 10)  # Change 10 to the desired number of items per page
    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        blog_posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category_detail = get_object_or_404(BlogCategory, pk=category_id)
    blogs = Blog.objects.filter(category=category_detail)
    return render(request, 'blog/category.html', {'category_detail': category_detail, 'blogs': blogs})

def about(request):
    aboutus = aboutUs.objects.all()
    return render(request, 'about.html', {'about':aboutus})

def post(request):
    return render(request, 'blog/post.html')

def post_detail(request):
    return render(request, 'blog/post_detail.html')


def contact(request):
    return render(request, 'contact.html')


def signUp(request):
     if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            # Check if username is available
            if User.objects.filter(username=username).exists():
                return render(request, 'home.html', {'error_message': 'Username already taken'})
            else:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                return redirect('home')  # Redirect to home page after registration
        else:
            return render(request, 'signUp.html', {'error_message': 'Passwords do not match'})
        
     return render(request, 'signUp.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect back to the login page with an error message
        
    return render(request, 'user_auth/login.html')