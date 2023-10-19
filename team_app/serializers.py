from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.reverse import reverse

from .models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    team_url = serializers.HyperlinkedIdentityField(view_name='team-detail')

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'team_url']

    def validate_name(self, value):
        """validation of the "name" field - the use of special characters is not allowed"""

        if not slugify(value):
            raise serializers.ValidationError('Special characters are not allowed in the title.')
        return value

    def to_representation(self, instance):
        """for better front-end data readability, I redefined this method:
        added urls, changed the name of the fields """

        representation = super().to_representation(instance)
        members_representation = []

        for person in instance.members.all():
            member_representation = {
                'person_id': person.id,
                'person_name': person.name,
                'person_url': reverse('person-detail', args=[person.id], request=self.context.get('request'))
            }
            members_representation.append(member_representation)
        representation["members"] = members_representation
        representation['total_members'] = len(members_representation)
        return representation


class PersonSerializer(serializers.ModelSerializer):
    person_url = serializers.HyperlinkedIdentityField(view_name='person-detail')

    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'email', 'teams', 'person_url']

    def to_representation(self, instance):
        """for better front-end data readability, I redefined this method:
        added urls, changed the name of the fields """

        representation = super().to_representation(instance)
        teams_representation = []

        for team in instance.teams.all():
            team_representation = {
                'team_id': team.id,
                'team_name': team.name,
                'team_url': reverse('team-detail', args=[team.id], request=self.context.get('request'))
            }
            teams_representation.append(team_representation)

        representation['teams'] = teams_representation
        representation['amount_teams'] = len(teams_representation)
        return representation
