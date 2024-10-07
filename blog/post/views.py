from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import Article
from django.contrib import messages

# Create your views here.
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password == password_confirm:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful.')
                auth_login(request, user)
                return redirect('home')
            except:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def home(request):
    posts = Article.objects.all()
    top = posts[0]
    return render(request, 'index.html', {'posts': posts, 'top': top})

def view_article(request, title):
    article = get_object_or_404(Article, title=title)
    return render(request, 'view_article.html', {'article': article})

def like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user.is_authenticated:
        article.likes += 1
        article.save()
        return redirect('view_article', article_id=article_id)
    else:
        messages.error(request, 'You need to be logged in to like an article.')
        return redirect('login')

