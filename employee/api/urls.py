from django.conf.urls import url

from .views import (
	EmployeeDetailAPIView,
	EmployeeListAPIView,
	EmployeeUpdateAPIView, 
	EmployeeDeleteAPIView,
	EmployeeCreateAPIView,
	)

urlpatterns = [
    url(r'^$', EmployeeListAPIView.as_view(), name='list'),
    url(r'^create/$', EmployeeCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>[\w-]+)/$', EmployeeDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', EmployeeUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', EmployeeDeleteAPIView.as_view(), name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
