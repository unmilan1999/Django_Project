from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'details.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'poster.html'
	fields = '__all__'