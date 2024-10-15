from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=3)

class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(read_only=True)
