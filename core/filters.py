import django_filters
from django import forms
from .models import LogbookMedical,Course,Professor,TreatmentMedical

class LogbookFilter(django_filters.FilterSet):


    logbook_course = django_filters.ModelChoiceFilter(field_name='logbook_course',lookup_expr='exact',queryset=Course.objects.all(),widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    logbook_professor = django_filters.ModelChoiceFilter(field_name='logbook_professor', lookup_expr='exact',queryset=Professor.objects.all(),widget=forms.Select(attrs={'class': 'form-control mb-3'}))




    class Meta:
        model = LogbookMedical
        fields = ['logbook_course', 'logbook_professor']



class TreatmentFilter(django_filters.FilterSet):



    treatment_course = django_filters.ModelChoiceFilter(field_name='treatment_course',lookup_expr='exact',queryset=Course.objects.all(),widget=forms.Select(attrs={'class': 'form-control mb-3'}))
   

    class Meta:
        model = TreatmentMedical
        fields = ['treatment_course']

