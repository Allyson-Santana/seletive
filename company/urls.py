from django.urls import path
from  . import views

urlpatterns = [
    path('new_company/', views.new_company, name='company_new_company'),
    path('companies/', views.companies, name='company_companies'),
    path('company/destroy/<int:id>', views.destroy, name='company_destroy'),
    path('company/<int:id>', views.findOne, name='company_findOne')
]
