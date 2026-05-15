from django.shortcuts import render, redirect
from .models import teacher
from .models import unitoutline
from .forms import InputForm
from pypdf import PdfWriter, PdfReader #Joining PDFs
from reportlab.pdfgen import canvas #Generating PDfs
from reportlab.platypus import Paragraph,Image,Table #Generating PDfs
from django.http import FileResponse #Downloading files
from django.contrib.staticfiles.storage import staticfiles_storage #Working with static files
from io import BytesIO #Using Byte streams

# Create your views here.
def index(request):
    teach = teacher.objects.all()
    unit = unitoutline.objects.all()
    return render(request,"MyApp1/index.html",{'content': teach})
    #return render(request,"MyApp1/index.html",{'content': unit})

def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()

    return render(request, "MyApp1/input.html", {"form": form})

def generate_pdf_file():

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]

    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    table = Table(lines)

    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def generate_pdf_file2():

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Assessment Item 1:', 'Due Date:', 'Assessment Item 2:', 'Due Date:', 'Assessment Item 3:', 'Due Date:', 'Content Description')]

    unitoutlines = unitoutline.objects.all()

    for unit in unitoutlines:
        lines.append((unit.AssessmentItem1, unit.AssessmentItem1DueDate, unit.AssessmentItem2, unit.AssessmentItem2DueDate, unit.AssessmentItem3, unit.AssessmentItem3DueDate, unit.ContentDescription))

    table = Table(lines)

    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def report(request):
    pdf_file =  staticfiles_storage.path("solutions.pdf")
    try:        
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf_file2())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)
        
        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    except FileNotFoundError:
        response = FileResponse(generate_pdf_file2(), as_attachment=True, filename="no.pdf")

    return response