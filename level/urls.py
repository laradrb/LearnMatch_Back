from django.urls import include, path
from rest_framework import routers
from level import views


router = routers.DefaultRouter()
router.register('level', views.LevelView, 'level')


urlpatterns = [

    path('', include(router.urls))
]