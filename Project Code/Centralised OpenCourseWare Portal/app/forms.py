from django import forms

from .models import OpenCourse

class AddCourseForm(forms.ModelForm):
	class Meta:
		model = OpenCourse
