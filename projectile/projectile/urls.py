"""projectlie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from rest_framework_jwt import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='EasyLink API')

admin.site.site_header = "EasyLink"
admin.site.index_title = "EasyLink Administration Portal"


urlpatterns = [
    # Only for the logged in user
    url(r'^api/v1/', include('core.urls.public')),
    url(r'^api/v1/me/', include('core.urls.me')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_jwt_token),
    url(r'^api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # swagger api docs
    url(r'^api/docs/', schema_view),

    # admin panel
    url(r'admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
