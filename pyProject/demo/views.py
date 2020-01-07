from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def demo_show(request):
    student = Student.objects.order_by('fname')
    return render(request, 'demo/demo_show.html', {'student': student})

    
# Create your views here.