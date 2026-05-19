from django.urls import path
from .views import course_list,like_course

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<int:course_id>/like/', like_course, name='like_course'),
]