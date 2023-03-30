# Importo la clase LoginRequiredMixin para requerir que el usuario esté autenticado antes de acceder a ciertas vistas.
from django.contrib.auth.mixins import LoginRequiredMixin
# Importo la clase PermissionDenied para negar el permiso de un usuario si no tiene permiso para realizar una acción.
from django.core.exceptions import PermissionDenied
# Importo la función get_object_or_404 para obtener un objeto de una clase específica o, si no existe, generar un error 404.
from django.shortcuts import get_object_or_404
# Importo la función reverse_lazy para generar una URL de vista inversa que se resuelve cuando la vista se llama por primera vez en lugar de en la importación.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView, FormView
# Importo todos los formularios de PostsApp
from PostsApp.forms import *
# Importo el modelos Post para manejar los posts.
from PostsApp.models import Post
# Importo el modelo Profile para manejar los usuarios
from UsersApp.models import Profile


# Defino a clase UserCanDeleteOrUpdateMixin para asegurarme de que solo el usuario que creó una publicación pueda editarla o eliminarla.
class UserCanDeleteOrUpdateMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author.user != request.user:
            raise PermissionDenied("No tienes permiso para manipular este post.")
        return super().dispatch(request, *args, **kwargs)

# Defino la Vista ListaMisPosts, que muestra una lista de publicaciones del usuario actual.
class ListaMisPosts(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'lista_mis_posts.html'
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.profile).order_by('-fecha_creacion', "titulo")

# Defino la Vista PostDetalleMio, que muestra los detalles de una publicación creada por el usuario actual.
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

# Defino la Vista ListaPosts, que muestra una lista de todas las publicaciones en el sitio
class ListaPosts(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'lista_posts.html'
    
    def get_queryset(self):
        return Post.objects.order_by('-fecha_creacion', "titulo")

# Defino la Vista PostDetalle, que muestra los detalles de una publicación cualquiera.
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
 
# Defino la Vista PostBorrado, que permite al usuario eliminar una publicación que ha creado
class PostBorrado(UserCanDeleteOrUpdateMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('PostsApp:ListaMisPosts')
    context_object_name = 'post'
    template_name = 'post_borrado.html'

# Defino la Vista PostCreacion, que permite al usuario crear una nueva publicación.
class PostCreacion(LoginRequiredMixin, FormView):
    model = Post
    form_class = FormularioNuevoPost
    success_url = reverse_lazy('PostsApp:ListaMisPosts')
    template_name = 'post_creacion.html'
    
    def form_valid(self, form):
        perfil = Profile.objects.filter(user=self.request.user)[0]
        form.instance.author = perfil
        form.save()
        return super().form_valid(form)

# Defino la Vista PostEdicion, que permite al usuario editar una publicación que ha creado.
class PostEdicion(UserCanDeleteOrUpdateMixin, UpdateView):
    model = Post
    form_class = FormularioEdicionPost
    success_url = reverse_lazy('PostsApp:ListaMisPosts')
    template_name = 'post_edicion.html'