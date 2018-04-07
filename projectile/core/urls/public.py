from django.conf.urls import url
from djoser import views

from ..views import public

urlpatterns = [
    url(r'^password/reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(
        r'^password/reset/confirm/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    url(r'^activate/$', views.ActivationView.as_view(), name='activate_account'),
    url(r'^register/$', public.UserRegistration.as_view(), name="register"),
    url(r'^login/$', public.MeLogin.as_view(), name='login'),
    url(r'^logout/$', public.MeLogout.as_view(), name='logout')
]
