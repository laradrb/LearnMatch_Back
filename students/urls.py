from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LogoutView, CourseViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('api/v1/', include(router.urls)),
]
