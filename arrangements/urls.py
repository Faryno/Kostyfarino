
from django.urls import path, re_path
# from .views import current_datetime
from .views import *

urlpatterns = [
    path('time_now/', current_datetime),
    path('greeting/<str:name>', greeting),
    path('class_view/',Example.as_view())
]
