from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from PostsApp.models import Post

# Create your views here.
class ListaMisPosts(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'lista_mis_posts.html'
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.profile).order_by("fecha_creacion", "titulo")
