from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render_to_response

from blog.models import Article, Post


def home(request):
    articles = Article.objects.all()
    posts  = Post.objects.reverse().all().order_by('id')
    context = {
        'articles': articles,
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

def media(request):
    return render(request, 'blog/media.html')

def hot(request):
    return render(request, 'blog/hot.html')

def contacts(request):
    return render(request, 'blog/contacts.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})

def show_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post})

def лаб_3(request):
    return render(request, 'blog/лаб_3.html')

def lab_4(request):
    return render(request, 'blog/lab_4.html')