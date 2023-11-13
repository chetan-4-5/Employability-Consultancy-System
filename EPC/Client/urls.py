from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user, name='user'),
    path('user/userprofile/',views.userprofile, name='userprofile'),
    path('user/userprofile/editprofile/', views.editprofile,name='editprofile'),
    path('user/applications/',views.applications,name='applications'),
    path('user/jobsearch/',views.jobsearch,name='jobsearch'),
    path('user/assessment/',views.assessment,name='assessment'),
    path('careercounselling/',views.careercounselling, name='careercounselling'),
    path('questions/',views.questions_view,name='questions'),
    path('score/',views.score_view,name='score'),
    path('resume/',views.resume,name='resume')
]
