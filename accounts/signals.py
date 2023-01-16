from django.db.models.signals import post_save
from accounts.models import Profile
from core.models import Professor,Patient,Student



def create_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == '0':
        print(instance.user_type)
        Professor.objects.create(prof_user=instance,)
        print('Professor created!')
    elif created and instance.user_type == '1':
        print(instance.user_type)
        Student.objects.create(student_user=instance,)
        print('Student created!')
    elif created and instance.user_type == '2':
        print(instance.user_type)
        Patient.objects.create(patient_user=instance,)
        print('patient created!')

post_save.connect(create_profile, sender=Profile)





