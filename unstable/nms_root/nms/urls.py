from django.conf.urls import patterns, url

from nms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login/$', views.login_handler, name='login_handler'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^devices/add/$', views.device_add, name='device_add'),
    url(r'^devices/manage/$', views.devices_manage, name='device_manage'),
    url(r'^devices/(?P<device_id_request>\d+)/manage/$', views.device_manager, name='device_manager'),
    url(r'^devices/(?P<device_id_request>\d+)/modify/$', views.device_modify, name='device_modify'),
	url(r'^devices/(?P<device_id_request>\d+)/command_handler/', views.send_command, name='device_command_handler'),
    url(r'^settings/$', views.user_settings, name='user_settings'),
    url(r'^acl/$', views.acl, name='acl'),
    url(r'^acl/groups/$', views.acl_groups, name='acl_groups'),
    url(r'^acl/groups/handler$', views.acl_groups_handler, name='acl_groups_handler'),
    url(r'^acl/groups/(?P<acl_id>\d+)/manage$', views.acl_groups_manage, name='acl_groups_manage'),
    url(r'^acl/users$', views.acl_user, name='acl_user'),
    url(r'^acl/users/add$', views.acl_user_add, name='acl_user_add'),
    url(r'^acl/users/add/handler$', views.acl_user_add_handler, name='acl_user_add_handler'),
    url(r'^acl/users/(?P<acl_user>\d+)/manage$', views.acl_user_manage, name='acl_user_manage'), 
    url(r'^acl/users/(?P<acl_user>\d+)/manage/handler$', views.acl_user_manage_handler, name='acl_user_manage_handler'),   
    url(r'^acl/devices/$', views.acl_device, name='acl_device'),  
    url(r'^acl/devices/(?P<acl_id>\d+)/manage$', views.acl_device_manage, name='acl_device_manage'),
    url(r'^acl/(?P<acl_id>\d+)/handler', views.acl_handler, name='acl_handler'),
    url(r'^install/$', views.install, name='install'),
    url(r'^session/$', views.session_handler, name='session_handler'),
    url(r'^logout/$', views.logout_handler, name='logout_handler'),
	url(r'^query/', views.query, name='query'),
	url(r'^devices/(?P<device_id_request>\d+)/manage/ssh/$', views.device_ssh, name='device_ssh'),
	url(r'^init/$', views.init, name='init'),
    url(r'^license/$', views.license, name='license'),
	url(r'^manage_gendev', views.manage_gendev, name='manage_gendev'),
)
