from django.contrib import admin
from .models import Student,Patient,Professor,Course,DiagnosisMedical,TreatmentMedical,LogbookMedical

# Register your models here.


class ProfessorFilter(admin.ModelAdmin):
    list_display=("id","__str__","prof_created_at","prof_updated_at")
    list_filter=("prof_created_at","prof_created_at")
    list_display_links=("id","__str__")

class StudentFilter(admin.ModelAdmin):
    list_display=("id","__str__","student_created_at","student_updated_at")
    list_filter=("student_created_at","student_updated_at")
    list_display_links=("id","__str__")

class PatientFilter(admin.ModelAdmin):
    list_display=("id","__str__","patient_created_at","patient_updated_at")
    list_filter=("patient_created_at","patient_updated_at")
    list_display_links=("id","__str__")

class CourseFilter(admin.ModelAdmin):
    list_display=("id","__str__","course_created_at","course_updated_at")
    list_filter=("course_created_at","course_updated_at")
    list_display_links=("id","__str__")

class DiagnosisMedicalFilter(admin.ModelAdmin):
    list_display=("id","__str__","diagnosis_professor","diagnosis_patient","diagnosis_date","diagnosis_status")
    list_filter=("diagnosis_professor","diagnosis_patient","diagnosis_status")
    list_display_links=("id","__str__")



class TreatmentMedicalFilter(admin.ModelAdmin):
    list_display=("id","__str__","treatment_student","treatment_patient","treatment_course","treatment_date","treatment_status")
    list_filter=("treatment_student","treatment_patient","treatment_course","treatment_status")
    list_display_links=("id","__str__")

class LogbookMedicalFilter(admin.ModelAdmin):
    list_display=("id","__str__","logbook_patient","logbook_professor","logbook_course","logbook_status","logbook_date_Submitted","logbook_date_Approved")
    list_filter=("logbook_patient","logbook_professor","logbook_student","logbook_course","logbook_date_Submitted","logbook_date_Approved")
    list_display_links=("id","__str__")

admin.site.register(Professor,ProfessorFilter)
admin.site.register(Patient,PatientFilter)
admin.site.register(Student,StudentFilter)
admin.site.register(Course,CourseFilter)
admin.site.register(DiagnosisMedical,DiagnosisMedicalFilter)
admin.site.register(TreatmentMedical,TreatmentMedicalFilter)
admin.site.register(LogbookMedical,LogbookMedicalFilter)



