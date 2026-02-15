from rest_framework import viewsets, permissions
from .models import Profile, Project, ContactMessage
from .serializers import ProfileSerializer, ProjectSerializer, ContactMessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @action(detail=False, methods=['get'])
    def featured(self, request):
        qs = self.get_queryset().filter(featured=True)
        return Response(ProjectSerializer(qs, many=True).data)

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post', 'get']