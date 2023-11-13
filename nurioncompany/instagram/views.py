from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .customviews import *
from django.views.generic import ListView, DetailView, ArchiveIndexView
from django.http import HttpResponse, HttpRequest
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
