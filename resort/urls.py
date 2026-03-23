from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import StyledLoginForm
from .views import (
    AboutView,
    CatalogView,
    ContactView,
    HomeView,
    ProfileView,
    RegisterView,
    ResortDetailView,
    toggle_favorite,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', ResortDetailView.as_view(), name='resort_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('favorites/<int:pk>/', toggle_favorite, name='toggle_favorite'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name='resort/auth/login.html', authentication_form=StyledLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
