from django import forms
from .models import DiagnosisMedical,Course,Student,LogbookMedical,TreatmentMedical,Professor
from accounts.models import Profile
from datetime import date,timedelta
import datetime
from django.contrib.auth.models import Group


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




class AdminDiagnosisForm(forms.ModelForm):
        
        diagnosis_date=forms.DateTimeField(label="choose DateTime Diagnosis",required=False,widget=DateTimeIn(attrs={'class': 'form-control mb-3'}))
        diagnosis_professor=forms.ModelChoiceField(label='Select Professor',queryset=Professor.objects.all(), required=False,widget=forms.Select(attrs={'class': 'form-control mb-3'}))
        class Meta:
            model = DiagnosisMedical
            fields = ('diagnosis_date','diagnosis_professor')

class AdminCourseForm(forms.ModelForm):
    course_name=forms.CharField(label='Course Name', min_length=3,required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    course_img=forms.ImageField(label='Course Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))
    course_students=forms.ModelMultipleChoiceField(label='Select Students',queryset=Student.objects.all(), required=False,widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}))
    course_professors=forms.ModelMultipleChoiceField(label='Select Professors',queryset=Professor.objects.all(), required=False,widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = Course
        fields = ('course_name','course_img','course_students','course_professors')

user_type_data=(
    ('0','Professor'),
    ('1','Student'),
    ('2','Patient'),
)

countries_choices = (
    ('AFGHANISTAN', 'AFGHANISTAN'),
    ('ALBANIA', 'ALBANIA'),
    ('ALGERIA', 'ALGERIA'),
    ('ANDORRA', 'ANDORRA'),
    ('ANGOLA', 'ANGOLA'),
    ('ANGUILLA', 'ANGUILLA'),
    ('ANTARCTICA', 'ANTARCTICA'),
    ('ARGENTINA', 'ARGENTINA'),
    ('ARMENIA', 'ARMENIA'),
    ('AUSTRALIA', 'AUSTRALIA'),
    ('AUSTRIA', 'AUSTRIA'),
    ('AZERBAIJAN', 'AZERBAIJAN'),
    ('BAHAMAS', 'BAHAMAS'),
    ('BAHRAIN', 'BAHRAIN'),
    ('BANGLADESH', 'BANGLADESH'),
    ('BARBADOS', 'BARBADOS'),
    ('BELARUS', 'BELARUS'),
    ('BELGIUM', 'BELGIUM'),
    ('BELIZE', 'BELIZE'),
    ('BOLIVIA', 'BOLIVIA'),
    ('BRAZIL', 'BRAZIL'),
    ('BULGARIA', 'BULGARIA'),
    ('CAMEROON', 'CAMEROON'),
    ('CANADA', 'CANADA'),
    ('CHINA', 'CHINA'),
    ('COLOMBIA', 'COLOMBIA'),
    ('COMOROS', 'COMOROS'),
    ('CONGO', 'CONGO'),
    ('COSTA RICA', 'COSTA RICA'),
    ('CROATIA', 'CROATIA'),
    ('CUBA', 'CUBA'),
    ('CYPRUS', 'CYPRUS'),
    ('CZECH', 'CZECH REPUBLIC'),
    ('DENMARK', 'DENMARK'),
    ('DJIBOUTI', 'DJIBOUTI'),
    ('DOMINICAN', 'DOMINICAN REPUBLIC'),
    ('ECUADOR', 'ECUADOR'),
    ('EGYPT', 'EGYPT'),
    ('ERITREA', 'ERITREA'),
    ('ESTONIA', 'ESTONIA'),
    ('ETHIOPIA', 'ETHIOPIA'),
    ('FINLAND', 'FINLAND'),
    ('FRANCE', 'FRANCE'),
    ('GABON', 'GABON'),
    ('GAMBIA', 'GAMBIA'),
    ('GEORGIA', 'GEORGIA'),
    ('GERMANY', 'GERMANY'),
    ('GHANA', 'GHANA'),
    ('GREECE', 'GREECE'),
    ('GREENLAND', 'GREENLAND'),
    ('HUNGARY', 'HUNGARY'),
    ('ICELAND', 'ICELAND'),
    ('INDIA', 'INDIA'),
    ('INDONESIA', 'INDONESIA'),
    ('IRAN', 'IRAN'),
    ('IRAQ', 'IRAQ'),
    ('IRELAND', 'IRELAND'),
    ('ITALY', 'ITALY'),
    ('JAPAN', 'JAPAN'),
    ('JORDAN', 'JORDAN'),
    ('KAZAKHSTAN', 'KAZAKHSTAN'),
    ('KENYA', 'KENYA'),
    ('KIRIBATI', 'KIRIBATI'),
    ('North KOREA', "North KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),
    ('South KOREA', 'South KOREA, REPUBLIC OF'),
    ('KUWAIT', 'KUWAIT'),
    ('KYRGYZSTAN', 'KYRGYZSTAN'),
    ('LATVIA', 'LATVIA'),
    ('LEBANON', 'LEBANON'),
    ('LIBYAN', 'LIBYAN ARAB JAMAHIRIYA'),
    ('LIECHTENSTEIN', 'LIECHTENSTEIN'),
    ('LITHUANIA', 'LITHUANIA'),
    ('LUXEMBOURG', 'LUXEMBOURG'),
    ('MACAO', 'MACAO'),
    ('MACEDONIA', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),
    ('MADAGASCAR', 'MADAGASCAR'),
    ('MALAWI', 'MALAWI'),
    ('MALAYSIA', 'MALAYSIA'),
    ('MALDIVES', 'MALDIVES'),
    ('MALI', 'MALI'),
    ('MALTA', 'MALTA'),
    ('MOROCCO', 'MOROCCO'),
    ('MOZAMBIQUE', 'MOZAMBIQUE'),
    ('NEPAL', 'NEPAL'),
    ('NETHERLANDS', 'NETHERLANDS'),
    ('NIGERIA', 'NIGERIA'),
    ('NORWAY', 'NORWAY'),
    ('OMAN', 'OMAN'),
    ('PAKISTAN', 'PAKISTAN'),
    ('PALAU', 'PALAU'),
    ('PALESTINIAN', 'PALESTINIAN'),
    ('PANAMA', 'PANAMA'),
    ('PARAGUAY', 'PARAGUAY'),
    ('PERU', 'PERU'),
    ('PHILIPPINES', 'PHILIPPINES'),
    ('PITCAIRN', 'PITCAIRN'),
    ('POLAND', 'POLAND'),
    ('PORTUGAL', 'PORTUGAL'),
    ('QATAR', 'QATAR'),
    ('ROMANIA', 'ROMANIA'),
    ('RUSSIAN', 'RUSSIAN FEDERATION'),
    ('RWANDA', 'RWANDA'),
    ('SAUDI ARABIA', 'SAUDI ARABIA'),
    ('SENEGAL', 'SENEGAL'),
    ('SINGAPORE', 'SINGAPORE'),
    ('SLOVAKIA', 'SLOVAKIA'),
    ('SLOVENIA', 'SLOVENIA'),
    ('SOMALIA', 'SOMALIA'),
    ('SOUTH AFRICA', 'SOUTH AFRICA'),
    ('SPAIN', 'SPAIN'),
    ('SUDAN', 'SUDAN'),
    ('SWEDEN', 'SWEDEN'),
    ('SWITZERLAND', 'SWITZERLAND'),
    ('SYRIAN', 'SYRIAN ARAB REPUBLIC'),
    ('TAIWAN', 'TAIWAN'),
    ('TAJIKISTAN', 'TAJIKISTAN'),
    ('TANZANIA', 'TANZANIA'),
    ('THAILAND', 'THAILAND'),
    ('TUNISIA', 'TUNISIA'),
    ('TURKEY', 'TURKEY'),
    ('TURKMENISTAN', 'TURKMENISTAN'),
    ('UGANDA', 'UGANDA'),
    ('UKRAINE', 'UKRAINE'),
    ('UNITED ARAB EMIRATES', 'UNITED ARAB EMIRATES'),
    ('UNITED KINGDOM', 'UNITED KINGDOM'),
    ('UNITED STATES', 'UNITED STATES'),
    ('URUGUAY', 'URUGUAY'),
    ('UZBEKISTAN', 'UZBEKISTAN'),
    ('YEMEN', 'YEMEN'),

)

gender_choice=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)

class Dateinput(forms.DateInput):
    input_type='date'


class AdminRegisterForm(forms.ModelForm):

    name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    nationality=forms.ChoiceField(label="Nationality",choices=countries_choices,required=True, help_text='Required',error_messages={
        'required': 'Sorry, you will need Nationality'})
    mobile=forms.CharField(label="Mobile Phone",max_length=20,required=True, help_text='Required',error_messages={
        'required': 'Sorry, you will need Mobile Phone'})
    address=forms.CharField(label="Address",max_length=50,required=True, help_text='Required',error_messages={
        'required': 'Sorry, you will need Address'})
    gender=forms.ChoiceField(label="Gender", choices=gender_choice, required=True, help_text='Required',error_messages={
         'required': 'Sorry, you will need Gender'})

    birthdate=forms.DateField(label="Birth Date",required=True, help_text='Required',error_messages={
         'required': 'Sorry, you will need Birth Date'},widget=Dateinput)
    profile_img = forms.ImageField(label='Profile Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Profile Image'}))
    user_type=forms.ChoiceField(label="User Type", choices=user_type_data, required=True, help_text='Required',error_messages={
         'required': 'Sorry, you will need user-type'})
    usergroup=forms.ModelMultipleChoiceField(label='Select User Group',queryset=Group.objects.all(), required=True,widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = Profile
        fields = ('name', 'email','profile_img')

    def clean_username(self):
        name = self.cleaned_data['name'].lower()
        r = Profile.objects.filter(name=name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        
        if (datetime.date.today() - birthdate)// timedelta(days=365.2425) <= 3:
            raise forms.ValidationError('The date cannot be Set You Must Be 3 Years Old at Least!')
        return birthdate

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
        self.fields['mobile'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'YOUR MOBILE NUMBER'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'YOUR Address'})
        self.fields['birthdate'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['gender'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'YOUR Gender'})
        self.fields['nationality'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'YOUR Nationality'})
        self.fields['user_type'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'User Account Type'})
        self.fields['usergroup'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'User Group'})



class AdminEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3 bg-light', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))



    name = forms.CharField(
        label='name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Your name', 'id': 'form-lastname'}))
    nationality = forms.ChoiceField(
        label='nationality',choices=countries_choices,widget=forms.Select(
            attrs={'class': 'form-control mb-3', 'placeholder': 'nationality'}))

    mobile = forms.CharField(
        label='mobile', min_length=4, max_length=20, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Your mobile'}))

    address = forms.CharField(
        label='address', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Your address'}))

    gender = forms.ChoiceField(
        label='Gender',choices=gender_choice, widget=forms.Select(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Gender'}))

    birthdate = forms.DateField(
        label='Birth Date', widget=Dateinput(attrs={'class': 'form-control mb-3', 'placeholder': 'birthdate'}))
    profile_img = forms.ImageField(
        label='Profile Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Profile Image'}))

    class Meta:
        model = Profile
        fields = ('email','name','birthdate','nationality','mobile','address','gender','profile_img')


    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']

        if (datetime.date.today() - birthdate)// timedelta(days=365.2425) <= 3:
            raise forms.ValidationError('The date cannot be Set You Must Be 3 Years Old at Least!')
        return birthdate


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user_name'].required = True
        self.fields['email'].required = True

