from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='course_list')
def create_like(request,course_id):
    course = get_object_or_404()

