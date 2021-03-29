"""hr101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from content import views
from discussions import views as discussions_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.home, name='home'),
	path('signup/', accounts_views.signup, name='signup'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('community/', discussions_views.discussions, name='community'),
	path('education/', views.education, name='education'),
	path('course/<index>/', views.course, name='course'),
	path('course2/', views.course2, name='course2'),
	path('profile/', discussions_views.profile, name='profile'),
	path('community/<pk>/new/', discussions_views.new_topic, name='new_topic'),
	
	path('reset/', 
		 auth_views.PasswordResetView.as_view(
			template_name='password_reset.html',
			email_template_name='password_reset_email.html',
			subject_template_name='password_reset_subject.txt'
		),
		name='password_reset'),
	path('reset/done/', 
		 auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
	path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
	
	path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
	path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
