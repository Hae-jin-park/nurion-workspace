from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, UpdateView, CreateView
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import ProfileForm
# Create your views here.

User = get_user_model()

# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


profile = ProfileView.as_view()


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm

@login_required
def profile_update(request):
    try:
        # Profile.objects.get(user=request.user)
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })

# signup = CreateView.as_view(
#     model=User,
#     form_class=UserCreationForm,
#     success_url=settings.LOGIN_URL,
#     template_name = 'accounts/signup_form.html'
# )


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'accounts/signup_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        auth_login(self.request, user)
        return response


signup = SignupView.as_view()
