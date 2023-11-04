from django.shortcuts import render
from .models import Post

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
