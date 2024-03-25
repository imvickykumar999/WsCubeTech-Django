
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def course(request):
    data = {
        'title' : 'Course Details',
        'c_id' : 100
    }
    return render(request, 'course.html', data)

def course_detail(request, course_id):
    return HttpResponse(f'<h1>You have selected Course ID = {course_id}</h1> <br> <a href="/"><h2>Home</h2></a>')
