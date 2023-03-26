from django.contrib import admin
from UsersApp.models import Profile
from PostsApp.models import Post

admin.site.register(Profile)

admin.site.register(Post)