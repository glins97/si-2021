from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from core import views


urlpatterns = [

    url(r'^attachment/(?P<pk>[0-9]+)/$', views.attachment_detail),
    url(r'^attachment/$', views.attachment_list),

    url(r'^tag/(?P<pk>[0-9]+)/$', views.tag_detail),
    url(r'^tag/$', views.tag_list),

    url(r'^bookmark/(?P<pk>[0-9]+)/$', views.bookmark_detail),
    url(r'^bookmark/$', views.bookmark_list),

    url(r'^comment/(?P<pk>[0-9]+)/$', views.comment_detail),
    url(r'^comment/$', views.comment_list),

    url(r'^publication/(?P<pk>[0-9]+)/$', views.publication_detail),
    url(r'^publication/$', views.publication_list),

    url(r'^country/(?P<pk>[0-9]+)/$', views.country_detail),
    url(r'^country/$', views.country_list),

    url(r'^state/(?P<pk>[0-9]+)/$', views.state_detail),
    url(r'^state/$', views.state_list),

    url(r'^city/(?P<pk>[0-9]+)/$', views.city_detail),
    url(r'^city/$', views.city_list),

    url(r'^neighborhood/(?P<pk>[0-9]+)/$', views.neighborhood_detail),
    url(r'^neighborhood/$', views.neighborhood_list),

    url(r'^place/(?P<pk>[0-9]+)/$', views.place_detail),
    url(r'^place/$', views.place_list),

    url(r'^achievementtype/(?P<pk>[0-9]+)/$', views.achievementtype_detail),
    url(r'^achievementtype/$', views.achievementtype_list),

    url(r'^achievement/(?P<pk>[0-9]+)/$', views.achievement_detail),
    url(r'^achievement/$', views.achievement_list),

    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile_detail),
    url(r'^profile/$', views.profile_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
