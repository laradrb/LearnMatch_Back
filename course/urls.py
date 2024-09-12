from django.urls import include, path
from rest_framework import routers
from course import views


router = routers.DefaultRouter()
router.register('course', views.CourseView, 'course')


urlpatterns = [

    path('', include(router.urls))
]
