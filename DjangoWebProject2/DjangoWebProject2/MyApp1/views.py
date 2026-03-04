from django.shortcuts import render
from .models import teacher

# Create your views here.
def index(request):
    teach = teacher.objects.all()

    return render(request,"HelloDjangoApp/index.html",{'content': teach})