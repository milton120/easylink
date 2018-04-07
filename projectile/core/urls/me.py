from django.conf.urls import url, include
from djoser import views

from ..views import private


urlpatterns = [
    # Move these urls below
    url(r'^password/$', views.SetPasswordView.as_view(), name='set_password'),
    url(r'^$', private.MeDetail.as_view(), name='me-details'),
]
