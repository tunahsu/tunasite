from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path(
        '',
        views.post_list,
        name='post_list'
    ),
    path(
        'tag/<str:tag_slug>/',
        views.post_list, name='post_list_by_tag'
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<str:slug>/',
        views.post_detail,
        name='post_detail'
    )
]