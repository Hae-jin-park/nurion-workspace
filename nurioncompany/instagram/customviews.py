from django.views.generic import DetailView
from .models import Post


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs
