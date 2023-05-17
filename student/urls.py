from django.urls import path
from .views import *


urlpatterns = [
    path("hello/" , Hello_students),
    path("dashboard/", StudentDashboard)
]