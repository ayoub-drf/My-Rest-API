from rest_framework.permissions import DjangoModelPermissions


class IsStaffEditorPermissions(DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            if user.has_perm('products.add_product'):
                return True
            return False
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if obj.owner.name == request.user.username:
            return True
        
        return False