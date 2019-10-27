from django.urls import path, re_path
from . import views
from .views import ContactDetailView
from .views import ContactCreateView, ContactUpdateView, ContactDeleteView, SignUpView
import re

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    #path('detail/<int:id>/', views.detail, name="detail"),
    path('detail/<int:pk>/', ContactDetailView.as_view(), name="detail"),
    path('search/', views.search, name="search"),
    path('contacts/create', ContactCreateView.as_view(), name="create"),
    path('contacts/update/<int:pk>/', ContactUpdateView.as_view(), name="update"),
    path('contacts/delete/<int:pk>/', ContactDeleteView.as_view(), name="delete"),
    path('signup/', SignUpView.as_view(), name="signup"),
    ]

