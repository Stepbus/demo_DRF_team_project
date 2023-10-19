from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from team_app.models import Team, Person
from team_app.serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Team.team_manager.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Person.person_manager.all()
    serializer_class = PersonSerializer



