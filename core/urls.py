from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, ProjectViewSet, ContactMessageViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contacts', ContactMessageViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]