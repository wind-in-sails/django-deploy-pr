from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AppUser, IssueDescription
from . import forms

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    users = AppUser.objects.order_by('first_name')
    cont = {'users' : users}
    return render(request, 'first_app/index.html', context=cont)

def sign_up_form(request):
    form = forms.UserForm()
    
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            print('SUCCESS')
            print('Name: ', name)
            print('Last Name: ', last_name)
            print('Email: ', email)
            print('Text: ', text)
            newUser = AppUser.objects.get_or_create(first_name=name, last_name=last_name, email = email)[0]
            newUser.text = text
            newUser.save()
        else:
            print("Failure")
    return render(request, 'first_app/user_form.html', {'form' : form})

def issue_report(request):
    form = forms.IssueDescriptionForm()

    if request.method == 'POST':
        form = forms.IssueDescriptionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Form is not valid!')
    return render(request, 'first_app/i_form.html', {'form' : form})

def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'first_app/registration.html', 
                    {'user_form': user_form,
                        'profile_form': profile_form,
                        'registered' : registered})

def user_login_to(request):
    print('we are here 0', request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('we are here 1')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} ans Password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'first_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_index'))

@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')

def home_index(request):
    return render(request, 'first_app/home.html')