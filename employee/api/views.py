from django.contrib.auth.models import User

from rest_framework import generics


from employee.models import Employee

from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView, 
	UpdateAPIView, 
	DestroyAPIView, 
	CreateAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly
from .pagination import VideotLimitOffsetPagination, VideoPageNumberPagination

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)


from django.db.models import Q

from .serializers import ( 
	EmployeeCreateSerializer, 
	EmployeeListSerializer, 
	EmployeeDetailSerializer
	)

from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeListAPIView(ListAPIView):
	queryset                = Employee.objects.all()
	serializer_class        = EmployeeListSerializer
	permission_classes = [AllowAny]



class EmployeeCreateAPIView(CsrfExemptMixin, CreateAPIView):
	authentication_classes = []
	queryset = Employee.objects.all()
	serializer_class = EmployeeCreateSerializer
	#permission_classes = [IsAuthenticated]



class EmployeeDetailAPIView(RetrieveAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeDetailSerializer
	lookup_field = 'id'
	permission_classes = [AllowAny]


class EmployeeUpdateAPIView(CsrfExemptMixin, RetrieveUpdateAPIView):
	authentication_classes = []
	queryset = Employee.objects.all()
	serializer_class = EmployeeCreateSerializer
	lookup_field = 'id'



class EmployeeDeleteAPIView(CsrfExemptMixin, DestroyAPIView):
	authentication_classes = []
	queryset = Employee.objects.all()
	serializer_class = EmployeeDetailSerializer
	lookup_field = 'id'





