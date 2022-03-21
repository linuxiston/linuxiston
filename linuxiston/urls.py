from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from django.urls import path

schema_view = get_swagger_view(title="Linuxiston API")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", schema_view),
]
