from django.contrib import admin
from blog.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierachy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created', 'post', 'active')
    list_filter = ('active', 'created', 'email')
    search_fields = ('username', 'email')
