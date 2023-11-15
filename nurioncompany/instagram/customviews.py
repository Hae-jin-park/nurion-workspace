from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from .forms import PostForm
from .models import Post


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅 저장 완료.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅 수정 완료.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = "instagram/post_confirm_delete.html"

    def get_success_url(self):
        messages.success(self.request, '포스팅 삭제 완료.')
        return reverse('instagram:post_list')

    # def form_valid(self, form):
    #     messages.success(self.request, '포스팅 삭제 완료.')
    #     return super().form_valid(form)
