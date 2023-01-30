from django.urls import path
from . import views


app_name = "core"


urlpatterns=[
    path('',views.home_index,name="home"),
    #Start Views OF Patient
    path('patient/show/all',views.patient_home_showall,name="patient_show_all"),
    path('patient/show/all/pending',views.patient_home_showall_pending,name="patient_showall_pending"),
    path('patient/show/diagnosis/<int:id>',views.patient_show_diagnosis,name="patient_show_single_diagnosis"),
    path('patient/show/diagnosis/cancel/<int:id>',views.patient_cancel_diagnosis_appointment,name="patient_cancel_diagnosis_appointment"),
    path('patient/show/treatment/<int:id>',views.patient_show_treatment,name="patient_show_single_treatment"),
    path('patient/show/treatment/cancel/<int:id>',views.patient_cancel_treatment_appointment,name="patient_cancel_treatment_appointment"),
    path('patient/show/treatment/pending/<int:id>',views.patient_pending_treatment_appointment,name="patient_pending_treatment_appointment"),
    path('patient/choose/diagnosis',views.patient_choose_diagnosises_appointment,name="patient_choose_diagnosises_appointment"),
    path('patient/book/diagnosis/<int:id>',views.patient_Book_diagnosises_appointment,name="patient_Book_diagnosises_appointment"),
    #END OF Views OF Patient

    #Start Views For Professor
    path('professor/show/all',views.professor_home_showall,name="professor_show_all"),
    path('professor/show/diagnosis/<int:id>',views.professor_show_single_diagnosis,name="professor_show_single_diagnosis"),
    path('professor/show/diagnosis/cancel/<int:id>',views.professor_cancel_dignosis_appointment,name="professor_cancel_dignosis_appointment"),
    path('professor/show/course/<int:id>',views.professor_show_single_course,name="professor_show_course"),
    path('professor/add/students/course/<int:id>',views.professor_add_student_to_course,name="professor_add_students"),
    path('professor/show/logbook/<int:id>',views.professor_show_single_logbook,name="professor_show_logbook"),
    path('professor/show/pending/logbook/<int:id>',views.professor_show_pending_logbook,name="professor_pending_logbook"),
    path('professor/approve/logbook/<int:id>',views.professor_approve_logbook,name="professor_approve_logbook"),
    path('professor/show/student/<int:id>',views.professor_show_student,name="professor_show_student"),
    path('professor/show/patient/<int:id>',views.professor_show_patient,name="professor_show_patient"),

    #END Views For Professor
    path('student/show/all',views.student_home_showall,name="student_show_all"),
    path('student/show/treatment/active/<int:id>',views.student_show_single_active_treatment,name="student_show_active_treatment"),
    path('student/show/treatment/cancel/<int:id>',views.student_cancel_treatment_appointment,name="student_cancel_treatment"),
    path('student/upload/logbookreport/treatment/<int:id>',views.student_write_logbook,name="student_write_logbook_report"),
    path('student/show/course/<int:id>',views.student_show_single_course,name="student_show_course"),
    path('student/show/logbook/active/<int:id>',views.student_show_single_active_logbook,name="student_show_active_logbook"),
    path('student/show/logbook/<int:id>',views.student_show_single_finsihed_logbook,name="student_show_logbook"),
    path('student/show/patient/<int:id>',views.student_show_single_patient,name="student_show_patient"),
    path('student/choose/treatment',views.student_choose_treatment_appointment,name="student_choose_treatment"),
    path('student/show/treatment/<int:id>',views.student_show_single_unreserved_treatment,name="student_show_treatment"),
    path('student/show/pending/treatments',views.student_show_all_pending_treatment,name="student_show_pending_treatments"),
    path('student/show/pending/treatment/<int:id>',views.student_show_single_pending_treatment,name="student_single_pending_treatment"),
    
    #END Views OF Student
    path('superadmin/show/alldiagnosis',views.admin_show_all_diagnosis,name="admin_show_all_diagnosis"),
    path('superadmin/Edit/diagnosis/<int:id>',views.admin_Edit_diagnosis,name="admin_edit_diagnosis"),
    path('superadmin/Create/diagnosis',views.admin_Create_diagnosis,name="admin_create_diagnosis"),
    path('superadmin/Delete/diagnosis/<int:id>',views.admin_Delete_diagnosis,name="admin_Delete_diagnosis"),
    
    path('superadmin/show/Courses',views.admin_show_all_courses,name="admin_show_all_courses"),
    path('superadmin/Edit/Course/<int:id>',views.admin_Edit_course,name="admin_edit_course"),
    path('superadmin/Create/Course',views.admin_Create_course,name="admin_create_course"),
    path('superadmin/Delete/Course/<int:id>',views.admin_Delete_course,name="admin_Delete_course"),
         
    path('superadmin/show/Users',views.admin_show_all_users,name="admin_show_all_users"),
    path('superadmin/Create/User',views.admin_Create_user,name="admin_Create_user"),
    path('superadmin/Delete/User/<int:id>',views.admin_Delete_user,name="admin_Delete_user"),
    path('superadmin/Edit/User/<int:id>',views.admin_Edit_user,name="admin_Edit_user"),
         
    
    
]


