from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from django.shortcuts import redirect, render

from .models import Post


class PostsList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post_edit.html', {})

    def post(self, request, *args, **kwargs):
        post = Post(
            type=request.POST['type'],
            name=request.POST['name'],
            text=request.POST['text'],
            author_id=request.user.id,
        )
        post.save()
        print(post.id)

        return redirect('/posts/')

    permission_required = ('news.add_post',)


