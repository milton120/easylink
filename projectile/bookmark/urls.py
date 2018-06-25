from django.conf.urls import url

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    url(r'^tag/$', views.TagList.as_view(),
        name="bookmark.tag-list"),
    url(r'^link/$', views.PublicLinkList.as_view(),
        name="bookmark.publick-link-list-create")
]