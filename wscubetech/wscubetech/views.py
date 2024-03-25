
from django.http import HttpResponse

def aboutus(request):
    return HttpResponse('About Us')

def contactus(request):
    return HttpResponse('Contact Us')
