from rest_framework import serializers
from .models import Owner, Product
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from api.validators import validate_name, unique_name

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # user_owner = UserPublicSerializer(source='user', read_only=True)
    user_related_products = UserPublicSerializer(source='user.product_set.all', many=True, read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)

    email = serializers.EmailField(write_only=True)

    name = serializers.CharField(validators=[unique_name])
    

    title = serializers.CharField(source='email', read_only=True)
    
    class Meta:
        model = Product
        fields = ('user_related_products', 'id', 'my_user_data', 'user', 'url', 'email', 'name', 'title', 'price', 'slug', 'owner', 'my_discount')


    def get_my_user_data(self, obj):
        return {
            'username': obj.user.username,
            'email': obj.user.email
        }

    # def validate_email(self, value):
    #     return value.upper()

    # def validate_name(self, value):
    #     qs = Product.objects.filter(name__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"this name ({value}) already in use")
    #     return value
    
    # def validate(self, attrs):
    #     email = attrs.get('email')
    #     if email:
    #         attrs['email'] = email.upper()
    #     return super().validate(attrs)

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        # instance.name = email
        instance.save()
        return instance
    

    def create(self, validated_data):
        email = validated_data.pop('email')
        return super().create(validated_data)


    def get_url(self, obj):
        # return f'<a href="/googl:e">>api/products/{obj.pk}</a>'
        request = self.context.get('request')
        print(request)

        if request is None:
            return None

        return reverse(viewname='product_detail', kwargs={'pk': obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
        return obj.discount