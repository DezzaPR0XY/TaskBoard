from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^login$', views.login),
]

from django.conf.urls import url
from mysite.core import views as core_views

urlpatterns = [
    ...
    url(r'^signup/$', core_views.signup, name='signup'),
]