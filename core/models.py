# Create your models here.
from accounts.models import Profile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

def Course_image_upload(instance,filename):
    txt='imgCourse_'
    imagename,extension=filename.split('.')
    return "Courses/%s%s.%s"%(txt,instance.id,extension)

def logbook_report_upload(instance,filename):
    txt='filereport_'
    imagename,extension=filename.split('.')
    return "Uploads/%s%s.%s"%(txt,instance.id,extension)




class Professor(models.Model):
    prof_user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    prof_created_at = models.DateTimeField(auto_now_add=True)
    prof_updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    def __str__(self):
        return "Prof:"+str(self.prof_user)

class Student(models.Model):
    student_user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    student_created_at = models.DateTimeField(auto_now_add=True)
    student_updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    def __str__(self):
        return "Student:"+str(self.student_user)

class Patient(models.Model):
    patient_user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    patient_created_at = models.DateTimeField(auto_now_add=True)
    patient_updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return "Patient:"+str(self.patient_user)






class Course(models.Model):
    course_name=models.CharField(_("Course_Name"), max_length=50)
    course_img=models.ImageField(upload_to="Course_image_upload",default="course.png")
    course_created_at = models.DateTimeField(auto_now_add=True)
    course_updated_at = models.DateTimeField(auto_now=True)
    course_students=models.ManyToManyField(Student, verbose_name=_("course students"),blank=True)
    course_professors=models.ManyToManyField(Professor, verbose_name=_("Course Professors"),blank=True)
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    def __str__(self):
        return self.course_name


diagnosis_status_choices=(
    ('0','Created'),
    ('1','ReservedByPatient'),
    ('2','CancelledByPatient'),
    ('3','CancelledByProfessor'),
    ('4','FinsishedByProfessor'),
)
class DiagnosisMedical(models.Model):
    diagnosis_date=models.DateTimeField(blank=True,null=True)
    diagnosis_professor=models.ForeignKey(Professor, verbose_name=_("Diagnosis Professor"), on_delete=models.CASCADE,blank=True,null=True)
    diagnosis_course= models.ManyToManyField(Course, verbose_name=_("Diagnosis Course"),blank=True)
    diagnosis_patient=models.ForeignKey(Patient, verbose_name=_("Diagnosis Patient"), on_delete=models.CASCADE,blank=True,null=True)
    patient_chart=models.CharField(_("Patient Chart"), max_length=100,blank=True,null=True)
    patient_xray=models.ImageField(upload_to="Patient_Xray_upload",blank=True,null=True)
    diagnosis_status = models.CharField(_("Diagnosis Status"),default=diagnosis_status_choices[0],choices=diagnosis_status_choices, max_length=10)
    class Meta:
        verbose_name = "diagnosis"
        verbose_name_plural = "diagnosises"
    def __str__(self):
        return "Diagnosis:"+str(self.diagnosis_patient)+str(self.diagnosis_date)


treatment_status_choices=(
    ('0','Created'),
    ('1','ReservedByStudent'),
    ('2','CancelledByPatient'),
    ('3','PendingByPatient'),
    ('4','CancelledByStudent'),
    ('5','FinsishedByStudent'),
)
class TreatmentMedical(models.Model):
    treatment_date=models.DateTimeField(blank=True,null=True)
    treatment_student=models.ForeignKey(Student, verbose_name=_("Treatment Student"), on_delete=models.CASCADE,blank=True,null=True)
    treatment_diagnosis=models.ForeignKey(DiagnosisMedical, verbose_name=_("Treatment Diagnosis"), on_delete=models.SET_NULL,blank=True,null=True)
    treatment_status=models.CharField(_("Treatment Status"),default=treatment_status_choices[0],choices=treatment_status_choices, max_length=10)
    treatment_patient=models.ForeignKey(Patient, verbose_name=_("Treatment Patient"), on_delete=models.CASCADE,blank=True,null=True)
    treatment_course=models.ForeignKey(Course, verbose_name=_("Treatment Course"), on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        verbose_name = "treatment"
        verbose_name_plural = "treatments"
    def __str__(self):
        return "Treatment For Patient:"+str(self.treatment_patient)+str(self.treatment_date)


logbook_status_choices=(
    ('0','Created'),
    ('1','SubmittedByStudent'),
    ('2','ApprovedByProfessor'),
)
class LogbookMedical(models.Model):
    logbook_date_Submitted=models.DateTimeField(blank=True,null=True)
    logbook_student=models.ForeignKey(Student, verbose_name=_("Logbook Student"), on_delete=models.CASCADE,blank=True,null=True)
    logbook_treatment=models.OneToOneField(TreatmentMedical, verbose_name=_("Logbook Treatment "), on_delete=models.SET_NULL,blank=True,null=True)
    logbook_status=models.CharField(_("Logbook Status"),default=logbook_status_choices[0],choices=logbook_status_choices, max_length=10)
    logbook_patient=models.ForeignKey(Patient, verbose_name=_("Logbook Patient"), on_delete=models.CASCADE,blank=True,null=True)
    logbook_professor=models.ForeignKey(Professor, verbose_name=_("Logbook Professor"), on_delete=models.CASCADE,blank=True,null=True)
    logbook_course=models.ForeignKey(Course, verbose_name=_("LogBook Course"), on_delete=models.CASCADE,blank=True,null=True)
    logbook_date_Approved=models.DateTimeField(blank=True,null=True)
    logbook_report=models.FileField(_("LogBook Report"), upload_to=logbook_report_upload,max_length=100,blank=True)
    class Meta:
        verbose_name = "Logbook"
        verbose_name_plural = "Logbooks"
    def __str__(self):
        return "Logbook For Student:"+str(self.logbook_student)+str(self.logbook_date_Submitted)


