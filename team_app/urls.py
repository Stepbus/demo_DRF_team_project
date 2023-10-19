from django.urls import path, include
from rest_framework.routers import DefaultRouter

from team_app import views

router = DefaultRouter()

router.register(r'teams', views.TeamViewSet)
router.register(r'people', views.PersonViewSet)


urlpatterns = [
    path('', include(router.urls)),
]