from django.urls import path
from .views import registr_view,login_view,login_required
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', registr_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),


]