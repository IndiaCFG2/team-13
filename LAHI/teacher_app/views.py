from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from admin_app.forms import UserForm_teacher, UserProfileInfoForm_teacher
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from teacher_app.forms import teacher_content_form
# Create your views here.
from twilio.rest import Client

def link(request):
    account_sid = 'ACeabc92d0d1275b9c8a37a2d873cbbe2b' 
    auth_token = 'a594ee70638acb5269afb6dafc09a3a2' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='sdfgbn',     
                              to='whatsapp:+919877479110' 
                          )
    print(message.sid)
 
 
 


def index(request):
    return render(request, "teacher_app/base.html")


def welcome(request):
    return render(request, "teacher_app/welcome.html")


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm_teacher(request.POST)
        profile_form = UserProfileInfoForm_teacher(request.POST)

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
        user_form = UserForm_teacher()
        profile_form = UserProfileInfoForm_teacher()

    return render(request, 'teacher_app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'teacher_app/content.html',)
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Wrong Username or password")
            print("Username {}".format(username))
            print("Password {}".format(password))
            return HttpResponse("Invalid credentials")

    else:
        return render(request, 'teacher_app/login.html',)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index.html'))


# def add_content(request):

#     if request.method == "POST":

#         form = teacher_content_form(request.POST)

#         if form.is_valid():
#             print('HIIII')
#             content = form.save(commit=False)

#             if 'files' in request.FILES:
#                 content.files = request.FILES['files']

#             content.save()
#             print('Done')
#         else:
#             print('HIIII2')
#             print(form.errors)

#     else:
#         form = teacher_content_form()
#         return render(request, 'teacher_app/content.html', {'form': form, })
