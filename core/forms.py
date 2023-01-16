from django import forms
from .models import DiagnosisMedical,Course,Student,LogbookMedical,TreatmentMedical

class ProfessorReferalForm(forms.ModelForm):
    diagnosis_course=forms.ModelMultipleChoiceField(label='Select Courses',queryset=Course.objects.all(),  required=True,widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}))
    patient_chart = forms.CharField(label='Patient Chart', min_length=10,required=True, max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    patient_xray=forms.ImageField(label='X-Ray Image',required=True,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = DiagnosisMedical
        fields = ('patient_chart','diagnosis_course','patient_xray')


class StudentADDForm(forms.ModelForm):
    course_students=forms.ModelMultipleChoiceField(label='Select Students',queryset=Student.objects.all(), required=False,widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}))


    class Meta:
        model = Course
        fields = ('course_students',)



class StudentSubmitReportForm(forms.ModelForm):
    logbook_report=forms.FileField(label='Upload Your Report',required=True,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = LogbookMedical
        fields = ('logbook_report',)

    
class DateTimeIn(forms.DateTimeInput):
    input_type='datetime-local'





class StudentTakeappointmentDateForm(forms.ModelForm):
    treatment_date=forms.DateTimeField(label="choose DateTime Treatment",required=True,widget=DateTimeIn(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = TreatmentMedical
        fields = ('treatment_date',)




