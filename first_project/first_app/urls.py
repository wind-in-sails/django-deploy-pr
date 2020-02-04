from django.urls import path
from first_app import views

# for template tagging
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registration, name='register'),
    path('home/', views.home_index, name='home_index'),
    path('user_login/', views.user_login_to, name='user_login'),
    path('issue/', views.issue_report, name='issue_report'),
    path('sign_up/', views.sign_up_form, name='signup'),
]