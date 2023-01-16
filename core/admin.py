from django.contrib import admin
from .models import Student,Patient,Professor,Course,DiagnosisMedical,TreatmentMedical,LogbookMedical

# Register your models here.
admin.site.register(Professor)
admin.site.register(Patient)
admin.site.register(Course)
admin.site.register(DiagnosisMedical)
admin.site.register(Student)
admin.site.register(TreatmentMedical)
admin.site.register(LogbookMedical)

