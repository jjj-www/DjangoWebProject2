
from django import forms
from .models import teacher
from .models import unitoutline

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class InputForm(forms.ModelForm):
    class Meta:
        model = unitoutline
        fields = ['AssessmentItem1', 'AssessmentItem1DueDate', 'AssessmentItem2', 'AssessmentItem2DueDate', 'AssessmentItem3', 'AssessmentItem3DueDate', 'ContentDescription', 'DeliveredAsVET']