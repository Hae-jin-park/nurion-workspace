from django.urls import path, register_converter
from . import views


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


register_converter(YearConverter, 'year')


app_name = 'instagram'  # for reverse url.

urlpatterns = [
    path('new/', views.post_new, name="post_new"),
    path('<int:pk>/update/', views.post_update, name="post_update"),
    path('<int:pk>/delete/', views.post_delete, name="post_delete"),
    path('', views.post_list, name="post_list"),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive')
]
