from django.http import Http404
from django.shortcuts import render,redirect
from django.urls import conf
from matplotlib.style.core import context

from  .models import Course,Student

def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses

    }
    return render(request, 'movie/course_list.html', context)

def like_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404("kechirasiz bizday kurs topilmadi")
    student = Student.objects.first()
    if student:
        if course in student.liked_courses.all():
            student.liked_courses.remove(course)
        else:
            student.liked_courses.add(course)

    return redirect('course_list')