from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Define your actual home view here
]
