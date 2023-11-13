from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
