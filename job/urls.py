from django.urls import path
from  . import views

urlpatterns = [
    path('new_job/', views.new_job, name='new_job')
]

