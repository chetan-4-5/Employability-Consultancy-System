from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
import psycopg2
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from .models import User, Question
from .forms import SignUpForm, JobSearchForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Job


def home(request):
    return render(request, 'HomePage.html')


def user(request):
    return render(request, 'User.html')


def userprofile(request):
    return render(request, 'UserProfile.html')


def editprofile(request):
    return render(request, 'edit_profile.html')


def applications(request):
    return render(request, 'applications.html')


def jobsearch(request):
    if request.method == 'GET':
        form = JobSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            job_listings = Job.objects.filter(title__icontains=search_query)
            return render(request, 'JobSearchResults.html', {'job_listings': job_listings})
    else:
        form = JobSearchForm()
    return render(request, 'JobSearch.html', {'form': form})


def assessment(request):
    return render(request, 'Assessment.html')


def careercounselling(request):
    return render(request, 'CareerCounseeling.html')


def resume(request):
    return render(request, 'resume.html')


def questions_view(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})


def score_view(request):
    questions = Question.objects.all()
    score = 0

    for question in questions:
        selected_choice = request.POST.get(question.question_text)
        if selected_choice == question.correct_choice:
            score += 1

    return render(request, 'score.html', {'score': score})


@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        valid = authenticate(request, email=email, password=password)
        if valid is not None:
            auth_login(request, valid)
            return redirect('user')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'Login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'Login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
            user = User(email=email, password=password)
            user.save()
            return render(request, 'Login.html')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
