from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

schema_view = get_swagger_view(title="Linuxiston API")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # allauth
    path('logout/', LogoutView.as_view(), name='logout'),
    path("api2/", schema_view),
    path("", include("apps.blog.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
# else:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)