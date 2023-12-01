"""
URL configuration for hr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from hr_app import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('personal.html', views.personal),
    path('add_employer.html', views.add_employer),
    path('employer_list.html', views.employer_list),
    path('edit_employer.html', views.edit_employer),
    path('end_edit_employer.html', views.end_edit_employer),
    path('delete_employer.html', views.delete_employer),
    path('end_delete_employer.html', views.end_delete_employer),
    path('add_info.html', views.add_info),
    path('managing_job_directory.html', views.managing_job_directory),
    path('add_position.html', views.add_position),
    path('add_position_info.html', views.add_position_info),
    path('edit_position.html', views.edit_position),
    path('delete_position.html', views.delete_position),
    path('select_edit_employer.html', views.select_edit_employer),
    path('position_list.html', views.position_list),
    path('select_edit_position.html', views.select_edit_position),
    path('end_edit_position.html', views.end_edit_position),
    path('end_delete_position.html', views.end_delete_position),
]
