from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import ProjectAPIView, TaskAPIView, ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    #path('projects/', ProjectAPIView.as_view()),
    path('tasks/<int:numero>/', TaskAPIView.as_view()),
]

urlpatterns += router.urls
#urlpatterns = format_suffix_patterns(urlpatterns)