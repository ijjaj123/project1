from django.shortcuts import render
from .models import Student,Games

# Create your views here.
def index(request):
    students=Student.objects.all()
    context ={'students':students}
    return render(request, 'index.html',context)