from django.conf.urls import url

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    url(r'^tag/$', views.TagList.as_view(),
        name="bookmark.tag-list"),
    url(r'^private/category/$', views.CategoryList.as_view(),
        name="category-list-create"),
    url(r'^private/category/(?P<slug>[\w-]+)/$', views.CategoryDetails.as_view(),
        name="category-details"),
    url(r'^link/$', views.PublicLinkList.as_view(),
        name="bookmark.public-link-list-create"),
    url(r'^private/link/$', views.UserLinkList.as_view(),
        name="bookmark.private-link-list")
]