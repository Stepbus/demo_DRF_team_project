from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from team_app import views

schema_view = get_schema_view(
    openapi.Info(
        title="TEAM and MEMBERS API",
        default_version='v1',
        description="SWAGGER documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('', include("admin_users_app.urls")),
    path('admin/', admin.site.urls),
    path('api/', include("team_app.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
