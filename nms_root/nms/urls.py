from django.conf.urls import patterns, url

from nms import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^register$', views.register, name='register'),
    # ex: /polls/5/results/
    url(r'^nms-admin/$', views.nms_admin, name='nms_admin'),
    # ex: /polls/5/vote/
    url(r'^nms-admin/login$', views.nms_admin_login, name='nms_admin_login'),
    url(r'^nms-admin/add-device/$', views.nms_admin_add_device, name='nms_admin_add_device'),
)