from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .customviews import *
from django.views.generic import ListView, DetailView, ArchiveIndexView
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from .forms import PostForm
# Create your views here.


# def post_list(request):
#     qstr = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qstr = qstr.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qstr,
#         'q': q,
#     })
# post_list = ListView.as_view(model=Post, paginate_by=10)


# post_list = ListView.as_view(model=Post)


post_list = PostListView.as_view()

# def post_detail(request):
#     pass
# post_detail = DetailView.as_view(
#     model=Post, queryset=Post.objects.filter(is_public=True))
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })
post_detail = PostDetailView.as_view()


# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at')


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인 User Instance
            post.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'instagram/post_form.html', {
        'form': form,
    })


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    #작성자 check Tip
    if post.author != request.user:
        messages.error(request, '작성자만 수정할 수 있습니다.')
        return redirect(post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'instagram/post_form.html', {
        'form': form,
    })
