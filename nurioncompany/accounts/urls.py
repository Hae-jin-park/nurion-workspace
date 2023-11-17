from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .forms import LoginAuthForm
urlpatterns = [
    path('login/', LoginView.as_view(
      form_class=LoginAuthForm,
      template_name='accounts/login_form.html'), name="login"),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
