from django.shortcuts import render, redirect
from .models import teacher
from .models import unitoutline
from .forms import InputForm

# Create your views here.
def index(request):
    teach = teacher.objects.all()
    return render(request,"MyApp1/index.html",{'content': teach})

def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()

    return render(request, "MyApp1/input.html", {"form": form})