# Create your models here.
from datetime import date,timedelta
from django.db import models
from project import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.core.exceptions import ValidationError

def profile_image_upload(instance,filename):
    txt='imgprofile_'
    imagename,extension=filename.split('.')
    return "profiles/%s%s.%s"%(txt,instance.id,extension)



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

gender_choice=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)

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
class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nationality=models.CharField(max_length=50,choices=countries_choices)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=gender_choice)
    birthdate=models.DateField(_("Birth Date"),blank=False,null=True)
    user_type = models.CharField(default=user_type_data[2], choices=user_type_data,max_length=256)
    profile_img=models.ImageField(upload_to="profile_image_upload",default="profile2.png")
 

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','birthdate']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if  (datetime.date.today() - self.birthdate)// timedelta(days=365.2425) <= 3 :
            raise ValidationError("The date cannot be Set He Must Be 3 Years Old at Least!")
        super(Profile, self).save(*args, **kwargs)

# @receiver(post_save,sender=Profile)
# def create_patient_profile(sender,instance,created,**kwargs):
#     if created:
#         Patient.objects.create(patient_img=instance)


