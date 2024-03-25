
from django.http import HttpResponse

def home(request):
    return HttpResponse('Click <a href="/course-detail/">here</a> for Course Details')

def course(request):
    return HttpResponse('Let, Course ID = <a href="/course-detail/100">100</a>')

def course_detail(request, course_id):
    return HttpResponse(f'You have selected Course ID = {course_id}')
