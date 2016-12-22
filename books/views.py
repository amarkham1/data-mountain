from django.utils import timezone
import datetime
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from blog.settings import CATEGORY_TEMPLATES
from django.contrib.auth.decorators import login_required
	
def home(request):
	posts = Post.objects.order_by('-published_date')
	return render(request, 'blog/home.html', {'posts': posts})
	
def pt_detail(request, slug, category):
    post = get_object_or_404(Post, slug=slug, category__slug=category)
	#posts = Post.objects.filter(category__slug=category)
    template = CATEGORY_TEMPLATES.get(post.category.slug)
    return render(request, template, {'post': post})

def bt_detail(request, slug, category):
	post = get_object_or_404(Post, slug=slug, category__slug=category)
	template = CATEGORY_TEMPLATES.get(post.category.slug)
	return render(request, template, {'post': post})

def resources(request):
	post = get_object_or_404(Post, slug='resources')
	return render(request, 'blog/resources.html', {'post': post})

@login_required	
def post_draft_list(request):
    ptpost = Post.objects.filter(published_date__isnull=True, category__slug='progresstracker').order_by('created_date')
    btpost = Post.objects.filter(published_date__isnull=True).exclude(category__slug='progresstracker').exclude(category__slug='resources').order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'btpost': btpost, 'ptpost': ptpost})

    #return render(request, 'blog/post_draft_list.html', {'bt_posts': bt_posts, 'pt_posts': pt_posts})
    
@login_required	
def post_publish(request, slug, category):
    post = get_object_or_404(Post, slug=slug, category__slug=category)
    post.publish()
    template = CATEGORY_TEMPLATES.get(post.category.slug)
    return render(request, template, {'post': post})

@login_required	
def post_remove(request, slug, category):
    post = get_object_or_404(Post, slug=slug, category__slug=category)
    post.delete()
    if post.category == 'progresstracker':
        return redirect('progresstracker')
    else:
        return redirect('blogtopics')

def compsci(request):
	posts = Post.objects.filter(category__slug='computer-science', published_date__isnull=False).order_by('-published_date')
	return render(request, 'blog/computerscience.html', {'posts': posts})
	
def datasci(request):
	posts = Post.objects.filter(category__slug='data-science', published_date__isnull=False).order_by('-published_date')
	return render(request, 'blog/datascience.html', {'posts': posts})

def other(request):
	posts = Post.objects.filter(category__slug='other', published_date__isnull=False).order_by('-published_date')
	return render(request, 'blog/other.html', {'posts': posts})
	
def progresstracker(request):
	posts = Post.objects.filter(category__slug='progresstracker', published_date__isnull=False).order_by('-published_date')
	return render(request, 'blog/progresstracker.html', {'posts': posts})
	
def blogtopics(request):
	posts = Post.objects.exclude(category__slug='progresstracker').filter(published_date__isnull=False).order_by('-published_date')
	return render(request, 'blog/blogtopics.html', {'posts': posts})
	
@login_required	
def post_new(request):
    if request.method == "POST":
	    form = PostForm(request.POST)
	    if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
            if post.category == 'progresstracker':
                return redirect('pt_detail', slug=post.slug, category=post.category)
            elif post.category == 'resources':
                return redirect('resources')
            else:
                return redirect('bt_detail', slug=post.slug, category=post.category)
    else:
		form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
	
@login_required		
def post_edit(request, slug, category):
    post = get_object_or_404(Post, slug=slug, category__slug=category)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if post.category == 'progresstracker':
                return redirect('pt_detail', slug=post.slug, category=post.category)
            elif post.category == 'resources':
                return redirect('resources')
            else:
                return redirect('bt_detail', slug=post.slug, category=post.category)
           
    else:
		form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
@login_required	 
def resources_post_edit(request):
    post = get_object_or_404(Post, slug='resources')
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('resources')
    else:
		form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})