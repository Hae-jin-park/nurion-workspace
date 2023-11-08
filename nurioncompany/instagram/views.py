from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
# Create your views here.


def post_list(request):
    qstr = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qstr = qstr.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list': qstr,
        'q': q,
    })


# post_list = ListView.as_view(model=Post)


# def post_detail(request):
#     pass
post_detail = DetailView.as_view(model=Post)


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
