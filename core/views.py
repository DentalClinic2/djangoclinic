from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ProfessorReferalForm,StudentADDForm,StudentSubmitReportForm,StudentTakeappointmentDateForm
from django.db.models import Count,Q,Max,Min
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users 
# Create your views here.

# View For displaying HomePage for all user


def home_index(request):
    return render(request, 'home.html')


# Views For Patient

# First For show all reserved diagnosis and Reserved Treatment Appointment
@login_required
@allowed_users(allowed_roles=['patients'])
def patient_home_showall(request):
    # Show only the diagnosises appointment that reserved By patient
    alldiagnosis = DiagnosisMedical.objects.filter(
        diagnosis_status=1, diagnosis_patient__patient_user__id=request.user.id)

    # show only the treatments Appointment  which student has choose this
    alltreatment = TreatmentMedical.objects.filter(
        treatment_status=1, treatment_patient__patient_user__id=request.user.id)
    context = {'ALLdiagnosis_Var': alldiagnosis,
               'Alltreatment_Var': alltreatment}
    return render(request, 'patient/patient_show_all.html', context)

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_home_showall_pending(request):
    # show only the treatments Appointment  which student has choose this
    all_pending_treatment = TreatmentMedical.objects.filter(
        treatment_status=3, treatment_patient__patient_user__id=request.user.id)
    context = {'all_pending_treatment_Var': all_pending_treatment}
    return render(request, 'patient/patient_show_all_pending.html', context)

# Second View for Patient is when he click on specific diagnosis with id Display single diagnosis Page

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_show_diagnosis(request, id):
    # Show only the single diagnosis appointment that reserved By patient
    single_diagnosis = DiagnosisMedical.objects.get(id=id)
    if request.user.id == single_diagnosis.diagnosis_patient.patient_user.id:
        context = {'single_diagnosis_Var': single_diagnosis}
        return render(request, 'patient/patient_single_diagnosis_appointment.html', context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_cancel_diagnosis_appointment(request, id):
    # Show only the single diagnosis appointment that reserved By patient
    diagnosis = DiagnosisMedical.objects.get(id=id, diagnosis_status=1)
    if request.user.id == diagnosis.diagnosis_patient.patient_user.id:
        diagnosis.diagnosis_patient = None
        diagnosis.diagnosis_status = 0
        diagnosis.save()
        messages.success(request, ("Your Diagnosis Cancelled Successfully!"))
        return redirect(reverse('core:patient_show_all'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_show_treatment(request, id):
    # Show only the single treatment appointment that reserved By patient and Reserved From Student
    single_treatment = TreatmentMedical.objects.get(id=id, treatment_status=1)
    if request.user.id == single_treatment.treatment_patient.patient_user.id:
        context = {'single_treatment_Var': single_treatment}
        return render(request, 'patient/patient_single_treatment_appointment.html', context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


# This View For Patient That Can cancel His Treatment Appointment and Send Email To the Student
@login_required
@allowed_users(allowed_roles=['patients'])
def patient_cancel_treatment_appointment(request, id):
    # cancel only the single treatment appointment that reserved By patient
    treatment = TreatmentMedical.objects.get(id=id, treatment_status=1)
    if request.user.id == treatment.treatment_patient.patient_user.id:
        subject = "CanceledAppointment By Patient" + \
            str(treatment.treatment_patient.patient_user.name)
        message = "Dear Student: "+str(treatment.treatment_student.student_user.name)+" We wanted to inform you that the patient "+str(treatment.treatment_patient.patient_user.name) + \
            " has canceled his treatment appointment. You can book another appointment from the available appointments.\n For more information You Can Contact With Patient : \n Patient Email : " + \
            str(treatment.treatment_patient.patient_user.email) + \
            " \n Patient Mobile : " + \
            str(treatment.treatment_patient.patient_user.mobile)
        student_email = treatment.treatment_student.student_user.email
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[student_email],
                  fail_silently=False)
        treatment.delete()
        messages.success(request, ("Your treatment Cancelled Successfully!"))
        return redirect(reverse('core:patient_show_all'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

# This View For Patient That Can Pending His Treatment Appointment and Send Email To the Student to inform him to change the Date

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_pending_treatment_appointment(request, id):
    # cancel only the single treatment appointment that reserved By patient
    treatment = TreatmentMedical.objects.get(id=id, treatment_status=1)
    if request.user.id == treatment.treatment_patient.patient_user.id:
        subject = "PendingAppointment By Patient" + \
            str(treatment.treatment_patient.patient_user.name)
        message = "Dear Student: "+str(treatment.treatment_student.student_user.name)+" We wanted to inform you that the patient "+str(treatment.treatment_patient.patient_user.name) + \
            " has suspended the appointment and asked you to change his treatment appointment.\n For more information You Can Contact With Patient : \n Patient Email : " + \
            str(treatment.treatment_patient.patient_user.email) + \
            " \n Patient Mobile : " + \
            str(treatment.treatment_patient.patient_user.mobile)
        student_email = treatment.treatment_student.student_user.email
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[student_email],
                  fail_silently=False)
        treatment.treatment_status = 3
        treatment.treatment_date = None
        treatment.save()
        messages.success(request, ("Your treatment Pending Successfully!"))
        return redirect(reverse('core:patient_show_all'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_choose_diagnosises_appointment(request):
    diagnosis = DiagnosisMedical.objects.filter(diagnosis_status=0)
    context = {'not_chosen_diagnosises_Var': diagnosis}
    return render(request, 'patient/patient_Book_diagnosis.html', context)

@login_required
@allowed_users(allowed_roles=['patients'])
def patient_Book_diagnosises_appointment(request, id):
    # Show only the single treatment appointment that reserved By patient and Reserved From Student
    single_diagnosis = DiagnosisMedical.objects.get(id=id, diagnosis_status=0)
    single_patient = Patient.objects.get(patient_user__id=request.user.id)
    single_diagnosis.diagnosis_patient = single_patient
    single_diagnosis.diagnosis_status = 1
    single_diagnosis.save()
    messages.success(request, ("Your treatment Cancelled Successfully!"))
    return redirect(reverse('core:patient_show_all'))

# End Views of Patient

#######################################################

# Views For Professor

@login_required
@allowed_users(allowed_roles=['professors'])
def professor_home_showall(request):
    # Show only the diagnosises appointment that reserved By patient
    allreserveddiagnosis = DiagnosisMedical.objects.filter(
        diagnosis_status=1, diagnosis_professor__prof_user__id=request.user.id)

    # show only the courses   which related to  this professor
    allcourses = Course.objects.filter(
        course_professors__prof_user__id=request.user.id)

    context = {'allreserved_diagnosis_Var': allreserveddiagnosis,
               'allcourses_Var': allcourses}
    return render(request, 'professor/professor_show_all.html', context)


# this view for show single dignosis which related to this professor and he can cancel the appoitment or referal to take treatment
#CLEAN AND WORKING METHOD
@login_required
@allowed_users(allowed_roles=['professors'])
def professor_show_single_diagnosis(request, id):
    single_diagnosis = DiagnosisMedical.objects.get(
        id=id, diagnosis_status=1, diagnosis_professor__prof_user__id=request.user.id)
    approved_logbook = LogbookMedical.objects.filter(
        logbook_status=2, logbook_patient=single_diagnosis.diagnosis_patient)
    if request.user.id == single_diagnosis.diagnosis_professor.prof_user.id:
        if request.method == 'POST':
            referalForm = ProfessorReferalForm(request.POST,request.FILES,instance=single_diagnosis)
            
            if referalForm.is_valid():

                dignosis_form=referalForm.save(commit=False)
                dignosis_form.diagnosis_status=4
                dignosis_form.save()
                referalForm.save_m2m()
                print('Succesfully Submit')

                for choosed_course in dignosis_form.diagnosis_course.all():
                    TreatmentMedical.objects.create(treatment_diagnosis=single_diagnosis,treatment_status=0,treatment_patient=single_diagnosis.diagnosis_patient,treatment_course=choosed_course)
                referalForm = ProfessorReferalForm()
  
                return redirect(reverse('core:professor_show_all'))

        else:
            referalForm = ProfessorReferalForm(instance=single_diagnosis)

        context = {'diagnosis_VAR': single_diagnosis,
                   'approved_logbook_VAR': approved_logbook,'diagnosis_form':referalForm}
        return render(request, 'professor/professor_show_single_diagnoise.html', context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

@login_required
@allowed_users(allowed_roles=['professors'])
def professor_cancel_dignosis_appointment(request, id):
    # cancel only the single treatment appointment that reserved By patient
    dignosis = DiagnosisMedical.objects.get(
        id=id, diagnosis_status=1, diagnosis_professor__prof_user__id=request.user.id)
    if request.user.id == dignosis.diagnosis_professor.prof_user.id:
        subject = "CanceledAppointment By Professor" + \
            str(dignosis.diagnosis_professor.prof_user.name)
        message = "Dear Patient: "+str(dignosis.diagnosis_patient.patient_user.name)+" We wanted to inform you that the Professor "+str(
            dignosis.diagnosis_professor.prof_user.name)+" has canceled Your Dignosis appointment.\n You can book another appointment from the available appointments"
        patient_email = dignosis.diagnosis_patient.patient_user.email
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[patient_email],
                  fail_silently=False)
        dignosis.delete()
        messages.success(request, ("Your Dignosis Cancelled Successfully!"))
        return redirect(reverse('core:professor_show_all'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")



@login_required
@allowed_users(allowed_roles=['professors'])
def professor_show_single_course(request,id):
    single_course=Course.objects.get(id=id,course_professors__prof_user__id=request.user.id)
    not_approved_logbooks=LogbookMedical.objects.filter(logbook_status=1,logbook_course=single_course,logbook_student__in=single_course.course_students.all())
    student_logbook=Student.objects.filter(logbookmedical__logbook_course__id=single_course.id,logbookmedical__logbook_status=2,logbookmedical__logbook_student__in=single_course.course_students.all()).annotate(completed_cases=Count("logbookmedical",distinct=True))
    context={'single_course_VAR':single_course,'not_approved_logbooks_VAR':not_approved_logbooks,'student_logbook_VAR':student_logbook}
    return render(request,"professor/professor_show_single_course.html",context)







@login_required
@allowed_users(allowed_roles=['professors'])
def professor_show_pending_logbook(request,id):
    single_pending_logbook=LogbookMedical.objects.get(id=id,logbook_status=1)
    professors=[]
    for instance in single_pending_logbook.logbook_course.course_professors.all():
        professors.append(instance.prof_user.id)
   
    if request.user.id in professors:
        context={'single_pending_logbook_VAR':single_pending_logbook}
        return render(request,"professor/professor_show_single_pending_logbook.html",context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

@login_required
@allowed_users(allowed_roles=['professors'])
def professor_show_single_logbook(request,id):
    single_logbook=LogbookMedical.objects.get(id=id,logbook_status=2)
    context={'single_logbook_VAR':single_logbook}
    return render(request,"professor/professor_show_single_logbook.html",context)


@login_required
@allowed_users(allowed_roles=['professors'])
def professor_approve_logbook(request,id):
    single_approved_logbook=LogbookMedical.objects.get(id=id,logbook_status=1)
    approved_professor = Professor.objects.get(prof_user__id=request.user.id)
    professors=[]
    for instance in single_approved_logbook.logbook_course.course_professors.all():
        professors.append(instance.prof_user.id)
   
    if request.user.id in professors and single_approved_logbook.logbook_professor is None:
        single_approved_logbook.logbook_professor = approved_professor
        single_approved_logbook.logbook_status=2
        single_approved_logbook.logbook_date_Approved = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        single_approved_logbook.save()
        messages.success(request, ("Logbook Approved Successfully!"))
        return redirect('core:professor_show_logbook',id=id)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")



@login_required
@allowed_users(allowed_roles=['professors'])
def professor_add_student_to_course(request,id):
    single_course=Course.objects.get(id=id,course_professors__prof_user__id=request.user.id)
    if request.method == 'POST':
        Studentform = StudentADDForm(request.POST,request.FILES,instance=single_course)
    
        if Studentform.is_valid():

            form=Studentform.save(commit=False)
            form.save()
            Studentform.save_m2m()
            print('Succesfully Submit')
            Studentform = StudentADDForm()
            return redirect('core:professor_show_course',id=id)

    else:
        Studentform = StudentADDForm(instance=single_course)

    context={'single_course_VAR':single_course,'student_form':Studentform}
    return render(request,"professor/professor_add_students.html",context)



@login_required
@allowed_users(allowed_roles=['professors'])
def professor_show_student(request,id):
    single_student=Student.objects.get(id=id)
    all_approved_student_logbook=LogbookMedical.objects.filter(logbook_student_id=single_student.id,logbook_status=2)
    professorcourse=Course.objects.filter(course_professors__prof_user__id=request.user.id)
    all_pending_student_logbook=LogbookMedical.objects.filter(logbook_student=single_student,logbook_status=1,logbook_course__in=professorcourse.all())
    context={'single_student_VAR':single_student,'all_approved_student_logbook_VAR':all_approved_student_logbook,'all_pending_student_logbook_VAR':all_pending_student_logbook,'professor_course_VAR':professorcourse}
    return render(request,"professor/professor_show_single_student.html",context)

@login_required
@allowed_users(allowed_roles=['professors'])
def professor_show_patient(request,id):
    single_patient=Patient.objects.get(id=id)
    all_approved_logbook=LogbookMedical.objects.filter(logbook_patient_id=single_patient.id,logbook_status=2)
    context={'single_patient_VAR':single_patient,'all_approved_logbook_VAR':all_approved_logbook}
    return render(request,"professor/professor_show_single_patient.html",context)

#EnD OF professor Views



#Start Of Student Views
@login_required
@allowed_users(allowed_roles=['students'])
def student_home_showall(request):
    AllReservedTreatment=TreatmentMedical.objects.filter(treatment_status=1,treatment_student__student_user__id=request.user.id)
    AllStudentcourse=Course.objects.filter(course_students__student_user__id=request.user.id).annotate(completed_cases=Count("logbookmedical",distinct=True,filter=Q(logbookmedical__logbook_status=2)))
    AllSubmittedlogBook=LogbookMedical.objects.filter(logbook_status=1,logbook_student__student_user__id=request.user.id)

    context = {'AllReservedTreatment_Var': AllReservedTreatment,'AllStudentcourse_Var': AllStudentcourse,'AllSubmittedlogBook_Var':AllSubmittedlogBook}
    return render(request, 'student/student_show_all.html', context)

@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_active_treatment(request,id):
    Activetreatment=TreatmentMedical.objects.get(id=id,treatment_student__student_user__id=request.user.id,treatment_status=1)
    ALLFinsishedLogbooks=LogbookMedical.objects.filter(logbook_status=2)
    context={'Activetreatment_VAR':Activetreatment,'ALLFinsishedLogbooks_VAR':ALLFinsishedLogbooks}
    return render(request, 'student/student_show_active_treatment.html', context)


@login_required
@allowed_users(allowed_roles=['students'])
def student_cancel_treatment_appointment(request,id):
    canceledtreatment=TreatmentMedical.objects.get(id=id,treatment_status=1,treatment_student__student_user__id=request.user.id)
    if request.user.id==canceledtreatment.treatment_student.student_user.id:
        subject = "CanceledAppointment By Student" +str(canceledtreatment.treatment_student.student_user.name)
        message = "Dear Patient: "+str(canceledtreatment.treatment_patient.patient_user.name)+" We wanted to inform you that the Student "+str(canceledtreatment.treatment_student.student_user.name)+" has canceled Your Treatment appointment.\n"
        patient_email = canceledtreatment.treatment_patient.patient_user.email
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[patient_email],
                  fail_silently=False)
        canceledtreatment.treatment_student=None
        canceledtreatment.treatment_status=0
        canceledtreatment.save()
        messages.success(request, ("Your Treatment Cancelled Successfully!"))
        return redirect(reverse('core:student_show_all'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")
        

@login_required
@allowed_users(allowed_roles=['students'])
def student_write_logbook(request,id):
    single_treatment=TreatmentMedical.objects.get(id=id,treatment_student__student_user__id=request.user.id,treatment_status=1)
    if request.method == 'POST':
        report_form = StudentSubmitReportForm(request.POST,request.FILES)
    
        if report_form.is_valid():


            report=report_form.save(commit=False)

            
            if report.logbook_report:
                LogbookMedical.objects.create(logbook_treatment=single_treatment,logbook_status=1,logbook_patient=single_treatment.treatment_patient,logbook_course=single_treatment.treatment_course,logbook_report=report.logbook_report,logbook_student=single_treatment.treatment_student,logbook_date_Submitted=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
                single_treatment.treatment_status=5
                single_treatment.save()
                print('Succesfully Submit')
                single_treatment.treatment_status=5
                single_treatment.save()
                
            return redirect('core:student_show_all')

    else:
        report_form = StudentSubmitReportForm()

    context={'single_treatment_VAR':single_treatment,'Report_Form_Var':report_form}
    return render(request,"student/student_write_logbook.html",context)

@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_course(request,id):
    single_course=Course.objects.get(id=id,course_students__student_user__id=request.user.id)
    Allfinsihedlogbooks=LogbookMedical.objects.filter(logbook_course=single_course,logbook_status=2,logbook_student__student_user__id=request.user.id)
    AllActiveTreatments=TreatmentMedical.objects.filter(treatment_course=single_course,treatment_status=1,treatment_student__student_user__id=request.user.id)
    context={'single_course_VAR':single_course,'Allfinsihedlogbooks_Var':Allfinsihedlogbooks,'AllActiveTreatments_VAR':AllActiveTreatments}
    return render(request,"student/student_show_single_course.html",context)

@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_active_logbook(request,id):
    notapprovedlogbook=LogbookMedical.objects.get(id=id,logbook_status=1,logbook_student__student_user__id=request.user.id)
    context={'notapprovedlogbook_VAR':notapprovedlogbook}
    return render(request,"student/student_single_active_logbook.html",context)

@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_finsihed_logbook(request,id):
    approvedlogbook=LogbookMedical.objects.get(id=id,logbook_status=2)
    context={'approvedlogbook_VAR':approvedlogbook}
    return render(request,"student/student_single_logbook.html",context)

@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_patient(request,id):
    single_patient=Patient.objects.get(id=id)
    approvedlogbook=LogbookMedical.objects.filter(logbook_status=2,logbook_patient=single_patient)

    context={'single_patient_VAR':single_patient,'approvedlogbook_VAR':approvedlogbook}
    return render(request,"student/student_show_patient.html",context)


@login_required
@allowed_users(allowed_roles=['students'])
def student_choose_treatment_appointment(request):
    studentcourses=Course.objects.filter(course_students__student_user__id=request.user.id)
    studentinstance=Student.objects.get(student_user__id=request.user.id)
    Reservedtreatment=TreatmentMedical.objects.filter(treatment_status=1,treatment_course__in=studentcourses.all(),treatment_student=studentinstance)

    reservedtreatmentcourse=[]
    for instance in Reservedtreatment.all():
        reservedtreatmentcourse.append(instance.treatment_course)

    notreservedtreatment=TreatmentMedical.objects.filter(treatment_status=0,treatment_course__in=studentcourses).exclude(treatment_course__in=reservedtreatmentcourse)




    context = {'notreservedtreatment_Var': notreservedtreatment,'Reservedtreatment_VAR':Reservedtreatment}
    return render(request, 'student/student_choose_treatment.html', context)




@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_unreserved_treatment(request,id):
    studentcourses=Course.objects.filter(course_students__student_user__id=request.user.id)
    studentinstance=Student.objects.get(student_user__id=request.user.id)
    Reservedtreatment=TreatmentMedical.objects.filter(treatment_status=1,treatment_course__in=studentcourses.all(),treatment_student=studentinstance)
    reservedtreatmentcourse=[]
    for instance in Reservedtreatment.all():
        reservedtreatmentcourse.append(instance.treatment_course)
    unreservedtreatment=TreatmentMedical.objects.exclude(treatment_course__in=reservedtreatmentcourse).get(id=id,treatment_status=0,treatment_course__in=studentcourses)
    ALLFinsishedLogbooks=LogbookMedical.objects.filter(logbook_status=2)

    if request.method == 'POST':
        DateTimeform = StudentTakeappointmentDateForm(request.POST,request.FILES)
    
        if DateTimeform.is_valid():

            form=DateTimeform.save(commit=False)
            unreservedtreatment.treatment_status=1
            unreservedtreatment.treatment_student=studentinstance
            unreservedtreatment.treatment_date=form.treatment_date
            unreservedtreatment.save()
            print('Succesfully Submit')
            return redirect('core:student_choose_treatment')

    else:
        DateTimeform = StudentTakeappointmentDateForm()

    
    context={'unreservedtreatment_VAR':unreservedtreatment,'ALLFinsishedLogbooks_VAR':ALLFinsishedLogbooks,'DateTimeform_VAR':DateTimeform}
    return render(request, 'student/student_show_treatment.html', context)


@login_required
@allowed_users(allowed_roles=['students'])
def student_show_all_pending_treatment(request):
    AllPendingTreatment=TreatmentMedical.objects.filter(treatment_status=3,treatment_student__student_user__id=request.user.id)
    context={'AllPendingTreatment_VAR':AllPendingTreatment}
    return render(request,"student/student_show_all_pending_treatment.html",context)

@login_required
@allowed_users(allowed_roles=['students'])
def student_show_single_pending_treatment(request,id):
    SinglePendingTreatment=TreatmentMedical.objects.get(id=id,treatment_status=3,treatment_student__student_user__id=request.user.id)
    if request.method == 'POST':
        DateTimeform = StudentTakeappointmentDateForm(request.POST,request.FILES)

        if DateTimeform.is_valid():
            if request.user.id==SinglePendingTreatment.treatment_student.student_user.id:


                form=DateTimeform.save(commit=False)
                SinglePendingTreatment.treatment_status=1
                SinglePendingTreatment.treatment_date=form.treatment_date
                SinglePendingTreatment.save()
                subject = "New-Appointment Date" 
                message = "Dear Patient: "+str(SinglePendingTreatment.treatment_patient.patient_user.name)+" We wanted to inform you that the Student "+str(SinglePendingTreatment.treatment_student.student_user.name)+" has Reserve Another Date For Your Treatment appointment.\n"+"\n the Treatment Will Be In"+str(SinglePendingTreatment.treatment_date)
                patient_email = SinglePendingTreatment.treatment_patient.patient_user.email
                send_mail(subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[patient_email],
                fail_silently=False)
                print('Succesfully Submit')
                return redirect('core:student_show_pending_treatments')
            else:
                return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")

    else:
        DateTimeform = StudentTakeappointmentDateForm()
    context={'SinglePendingTreatment_VAR':SinglePendingTreatment,'DateTimeform_VAR':DateTimeform}
    return render(request,"student/student_single_pending_treatment.html",context)



 
