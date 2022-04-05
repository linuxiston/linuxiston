from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title="Linuxiston API")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api2", schema_view),
    path("", include("apps.blog.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)