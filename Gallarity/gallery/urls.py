from django.urls import path, include # type: ignore
from .views import settings_view
from .views import about_view
from .views import terms_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_wallpapers, name='search'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('upload/',  views.upload, name='upload'),
    path('setting/', views.settings_view, name='setting'),
    path('about/', views.about_view, name='about'),
    path('terms/', views.terms_view, name='terms'),
]