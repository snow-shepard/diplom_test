from django.urls import path, re_path

from .views import *
from.import views

urlpatterns = [
    path('', index, name='home'),
    path('osago/', osago, name='osago'),
    path('isa/', isa, name='isa'),
    path('news/', views.news_list, name='news_list'),
    path('post/<int:news_id>/', views.news_detail, name='news_detail'),
    path('faq/', views.faq, name='faq'),
    path('osf/', views.osf, name='osf'),
    path('isf/', views.isf, name='isf'),
    path('contacts/', views.contacts, name='contacts'),
    path('pss/', views.pss, name='pss'),
]