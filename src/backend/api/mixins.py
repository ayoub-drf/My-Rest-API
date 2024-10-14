from .permissions import IsStaffEditorPermissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class StaffEditorPermissionsMixin():
    permission_classes = [IsAdminUser]

from products.models import Product

class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if not self.request.user.is_authenticated:
            return Product.objects.none()
        
        return qs.filter(**lookup_data)
    

# class OwnerQuerySet():
#     def get_queryset(self, *args, **kwargs):
#         lookup_data = {'owner': self.request.user.username}
#         qs = super().get_queryset(*args, **kwargs)

#         return qs.filter(**lookup_data)