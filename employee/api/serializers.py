from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from employee.models import Employee


#crear video.
class EmployeeCreateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['firstName', 'lastName', 'slug', 'email', 'mobileNumber', 'featured', ]

    def get_image(self, obj):
        return "/static/ang/assets/images/nature/4.jpg"

post_detail_url = HyperlinkedIdentityField(
		view_name='detail',
		lookup_field='slug',
		)


#lista de videos
class EmployeeListSerializer(ModelSerializer):
	class Meta:
		model = Employee
		fields = [ 'id', 'firstName', 'lastName', 'slug', 'email', 'mobileNumber', 'featured', 'createdAt', ]

		def filter_query(self, queryset):
			queryset = super(InvoiceViewSet)



#detalle del video
class EmployeeDetailSerializer(ModelSerializer):

	class Meta:
		model = Employee
		fields = ['id',  'firstName', 'lastName', 'slug', 'email', 'mobileNumber', 'featured', ]


