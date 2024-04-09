from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProjectAPIView, TaskAPIView

urlpatterns = [
    path('projects/', ProjectAPIView.as_view()),
    path('tasks/<int:numero>/', TaskAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)