from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from admin_app.forms import UserForm_student,UserProfileInfoForm_student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import review_form,get_contentForm
from admin_app.models import content_db
from .models import getContent
# from teacher_app.forms import teacher_content_form
# Create your views here.


def index(request):
    return render(request, "student/base.html")


def welcome(request):
    return render(request, "student/welcome.html")


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm_student(request.POST)
        profile_form = UserProfileInfoForm_student(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile_form.save(commit=False)

            registered = True
        else:
            print(user_form.errors)
            print(profile_form.errors)

    else:
        user_form = UserForm_student()
        profile_form = UserProfileInfoForm_student()

    return render(request, 'student/registers.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'student/content.html',)
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Wrong Username or password")
            print("Username {}".format(username))
            print("Password {}".format(password))
            return HttpResponse("Invalid credentials")

    else:
        return render(request, 'student/login.html',)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index.html'))

def review(request):
    if request.method == "POST":
        form=review_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=review_form()
    return render(request, "student/review.html",{'form':form})

# #def get_content(request):
#     #if request.method == "POST":
#        # form=get_contentForm(request.POST)
#         if form.is_valid():
#             sub=form.cleaned_data['subject']
#             ans=content_db.objects.get(subject=sub)
#         else:
#             print(form.errors)
#     else:
#         form=get_contentForm()
#         print("Hi!!")
#     return render(request, "student/get_content.html",{'form':form})

def get_content(request):
    if request.method == "POST":
        form=(request.POST)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            ans = content_db.objects.get(subject=sub)
        else:
            print(form.errors)
    else:
        form=get_contentForm()
    return render(request, "student/get_content.html",{'form':form})