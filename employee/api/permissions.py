from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message = 'No es dueño de este objecto'
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user