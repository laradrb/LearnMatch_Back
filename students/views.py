from django.shortcuts import render
from rest_framework import generics, permissions, views, status
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Course
from .serializer import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Token deleted"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)


class CourseFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='exact')
    difficulty = django_filters.CharFilter(lookup_expr='exact')
    time_required = django_filters.CharFilter(lookup_expr='exact')
    session_time = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Course
        fields = ['category', 'difficulty', 'time_required', 'session_time']

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseFilter