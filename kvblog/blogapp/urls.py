from django.urls import path
from blogapp import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('history/', views.history, name='history'),
    path('result/<int:id>/', views.create_result, name='result'),
    path('form/', views.create_form, name='form'),
    path('contacts/', views.create_contacts, name='contacts'),
]