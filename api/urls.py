from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TaskViewSet, UserViewSet, SprintViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('sprints', SprintViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
