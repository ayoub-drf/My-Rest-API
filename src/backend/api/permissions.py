from rest_framework.permissions import DjangoModelPermissions


class IsStaffEditorPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        user = request.user
        # I want to set some here
        if user.is_staff:
            if user.has_perm('products.add_product'):
                return True
    
            return False
        
        else:
            if user.has_perm('products.view_product'):
                return True
            return False
    
    def has_object_permission(self, request, view, obj):
        if obj.owner.name == request.user.username:
            return True
        
        return False