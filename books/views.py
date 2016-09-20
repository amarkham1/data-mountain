from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, render, get_object_or_404
	
def home(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'blog/home.html', {'posts': posts})
	
def pt_detail(request, slug):
	ptpost = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/pt_detail.html', {'ptpost': ptpost})
	
def progresstracker(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'blog/progresstracker.html', {'posts': posts})
	
def blogtopics(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'blog/blogtopics.html', {'posts': posts})
	
def resources(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'blog/resources.html', {'posts': posts})
	
def progresstracker_new(request):
	if request.method == "POST":
	    form = PostForm(request.POST)
	    if form.is_valid():
			ptpost = form.save(commit=False)
			ptpost.author = request.user
			ptpost.published_date = timezone.now()
			ptpost.save()
			return redirect('pt_detail', slug=ptpost.slug)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, slug):
	ptpost = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
	    form = PostForm(request.POST, instance=ptpost)
	    if form.is_valid():
	    	ptpost = form.save(commit=False)
	    	ptpost.author = request.user
	    	ptpost.published_date = timezone.now()
	    	ptpost.save()
	    	return redirect('pt_detail', slug=ptpost.slug)
	
	else:
		form = PostForm(instance=ptpost)
	return render(request, 'blog/post_edit.html', {'form': form})