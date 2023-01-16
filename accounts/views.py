from django.shortcuts import render
from django.contrib.auth.models import Group
# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


from .forms import RegistrationForm, UserEditForm
from .models import Profile
from .tokens import account_activation_token

from core.models import Patient




@login_required
def edit_details(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST,request.FILES,instance=request.user)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, "account/dashboard/edit_details.html", {"user_form": user_form})


@login_required
def show_details(request):
    profile = Profile.objects.get(email=request.user.email)
    return render(request,'account/dashboard/show_details.html',{'profilevar': profile})




def account_register(request):

    if request.user.is_authenticated:
         return redirect("accounts:show_details")

    if request.method == "POST":
        registerForm = RegistrationForm(request.POST,request.FILES)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data["email"]
            user.mobile = registerForm.cleaned_data["mobile"]
            user.nationality = registerForm.cleaned_data["nationality"]
            user.address = registerForm.cleaned_data["address"]
            user.birthdate = registerForm.cleaned_data["birthdate"]
            user.gender = registerForm.cleaned_data["gender"]
            #user.profile_img=registerForm.cleaned_data["profile_img"]
            user.set_password(registerForm.cleaned_data["password"])
            user.is_active = False
            user.user_type=2
            user.save()

            group=Group.objects.get(name='patients')
            user.groups.add(group)
            
            #Create Patient Account
            Patient.objects.create(
                patient_user=user,
                
            )
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string(
                "account/registration/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            user.email_user(subject=subject, message=message)
            return render(request, "account/registration/register_email_confirm.html", {"form": registerForm})
    else:
        registerForm = RegistrationForm()
    return render(request, "account/registration/register.html", {"form": registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Profile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("accounts:show_details")
    else:
        return render(request, "account/registration/activation_invalid.html")



@login_required
def deactivate_user(request):
    user = Profile.objects.get(email=request.user.email)
    user.is_active = False
    user.save()
    logout(request)
    return redirect("accounts:deactivate_confirmation")

