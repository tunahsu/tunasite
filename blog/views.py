from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post, Comment
from blog.forms import CommentForm

from taggit.models import Tag

def post_list(request, tag_slug=None):
    if tag_slug:
        tag = Tag.objects.filter(slug=tag_slug).first()
        post_list = Post.objects.filter(tags__in=[tag])
    else:
        post_list = Post.objects.all()

    tag_list = Tag.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'tag_list': tag_list
        }
    )

def post_detail(request, year, month, day, slug):
    post = Post.objects.filter(
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug
    ).first()
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm
    tag_list = Tag.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return redirect(request.path_info)

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
            'tag_list': tag_list
        }
    )
