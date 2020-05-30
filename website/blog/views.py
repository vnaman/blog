from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
)

def home(request):
    return render(request, 'blog/home.html')


class blogListView(LoginRequiredMixin, ListView):
    model = Post
    # queryset = Post.objects.first()
    template_name = 'blog/blog.html'
    context_object_name='posts'
    ordering = ['-date']

class blogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class blogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class blogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


