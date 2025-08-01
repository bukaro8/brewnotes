from django.urls import path
from .views import home, profile
from django.shortcuts import redirect
from allauth.socialaccount.providers.google.views import oauth2_login


def google_login_redirect(request):
    return redirect('socialaccount_login', provider='google')


urlpatterns = [
    path('', home, name='home'),
    path("accounts/login/", google_login_redirect),
    path('account/profile/', profile, name='profile'),

]
