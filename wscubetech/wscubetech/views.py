
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def course(request):
    return HttpResponse('Let, Course ID = <a href="/course-detail/100">100</a>')

def course_detail(request, course_id):
    return HttpResponse(f'You have selected Course ID = {course_id}')
