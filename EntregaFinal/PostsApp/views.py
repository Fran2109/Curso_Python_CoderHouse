from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from PostsApp.models import Post
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import DeleteView 
from django.urls import reverse_lazy

class UserCanDeleteMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.author.user)
        if obj.author.user != request.user:
            raise PermissionDenied("No tienes permiso para eliminar este post.")
        return super().dispatch(request, *args, **kwargs)


# Create your views here.
class ListaMisPosts(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'lista_mis_posts.html'
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.profile).order_by('-fecha_creacion', "titulo")

class PostDetalleMio(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detalle_mio.html'
    def get_context_data(self, *args, **kwargs):
        posts = Post.objects.filter(author=self.request.user.profile).order_by('-fecha_creacion', "titulo")
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        if(post not in list(posts)):
            raise PermissionDenied("No tienes permiso para ver este post.")
        post_index = list(posts).index(post)
        anterior_post = None
        posterior_post = None
        if post_index > 0:
            anterior_post = posts[post_index - 1]
        if post_index < len(posts) - 1:
            posterior_post = posts[post_index + 1]
        context = super().get_context_data(*args, **kwargs)
        context['post'] = post
        context['anterior_post'] = anterior_post
        context['posterior_post'] = posterior_post
        return context

class ListaPosts(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'lista_posts.html'
    
    def get_queryset(self):
        return Post.objects.order_by('-fecha_creacion', "titulo")

class PostDetalle(DetailView):
    model = Post
    template_name = 'post_detalle.html'
    
    def get_context_data(self, *args, **kwargs):
        posts = Post.objects.order_by('-fecha_creacion', "titulo")
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        post_index = list(posts).index(post)
        anterior_post = None
        posterior_post = None
        if post_index > 0:
            anterior_post = posts[post_index - 1]
        if post_index < len(posts) - 1:
            posterior_post = posts[post_index + 1]
        context = super().get_context_data(*args, **kwargs)
        context['post'] = post
        context['anterior_post'] = anterior_post
        context['posterior_post'] = posterior_post
        return context
    
class PostBorrado(UserCanDeleteMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('PostsApp:ListaMisPosts')
    context_object_name = 'post'
    template_name = 'post_borrado.html'
    
    
    
    
    
    
    
    
    
    
    
    
    