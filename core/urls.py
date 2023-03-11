"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# SWAGGER CONFIG
schema_view = get_schema_view(
    openapi.Info(
        title="AyolUchun API",
        default_version="v1",
        description="AyolUchun API for Intern",
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
                  # path('admin/', admin.site.urls),
                  path('course/', include("apps.course.urls")),
                  # path('payment/', include("apps.payment.urls")),
                  # path('dashboard/'), include("apps.dashboard.urls"),
                  # path('about/'), include("apps.about.urls"),
                  path('blog/', include('apps.blog.api.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('api/v1/', include('apps.course.urls')),
                  path("i18n/", include("django.conf.urls.i18n")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
