from django.conf.urls import include,url

from django.contrib import admin

from rest_api_test import views
admin.autodiscover()
urlpatterns = [
                url(r'^admin/', include(admin.site.urls)),
                url(r'^users/', views.UserList.as_view()),
                url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), ]
