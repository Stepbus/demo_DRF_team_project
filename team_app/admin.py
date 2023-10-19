from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Count

from team_app.models import Team, Person

"""for now, I have removed the registration of this model for better display in the admin panel """
admin.site.unregister(Group)


class TeamAdmin(admin.ModelAdmin):
    """added clickability for fields, filtering and the ability to search by specific fields"""

    list_display = ('id', 'name', 'total_members')

    list_display_links = ('id', 'name')

    search_fields = ['id', 'name']

    def get_queryset(self, request):
        """I override this method to create a new field
        "total_members" in the queryset and use it for filtering"""

        queryset = super().get_queryset(request)
        queryset = queryset.annotate(total_members=Count('members'))
        return queryset

    def total_members(self, obj):
        return obj.members.count()

    total_members.admin_order_field = 'total_members'
    total_members.short_description = 'Total Members'


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'total_teams')

    list_display_links = ('name', 'surname', 'email')

    list_filter = ('name', 'surname')

    search_fields = ['name', 'surname', 'email']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(total_teams=Count('teams'))
        return queryset

    def total_teams(self, obj):
        return obj.teams.count()

    total_teams.admin_order_field = 'total_teams'
    total_teams.short_description = 'Teams amount'


admin.site.register(Team, TeamAdmin)
admin.site.register(Person, PersonAdmin)
