from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Post, Response


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


    def post(self, request, *args, **kwargs):
        response = Response(
            whom_id=request.POST['author_id'],
            post_id=request.POST['post_id'],
            text=request.POST['text'],
            who_id=request.user.id,
        )
        response.save()
        mail = User.objects.get(id=request.POST['author_id'])
        print(mail.email)
        send_mail(
            subject=f'Отклик',
            message=request.POST['text'],
            from_email='fastaganim666@yandex.ru',
            recipient_list=[mail.email]
        )
        return redirect('/posts/')


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


class Response(ListView):
    model = Post
    ordering = 'name'
    template_name = 'responses.html'
    context_object_name = 'posts'
    paginate_by = 10



