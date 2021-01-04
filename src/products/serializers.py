from rest_framework import serializers
from src.products.models import Product

# class ProductSerializer(serializers.Serializer):
#     brand = serializers.CharField()
#     category = serializers.CharField()
#     name = serializers.CharField(max_length=50)
#     price = serializers.IntegerField()
#     rate = serializers.IntegerField()
#     slug = serializers.SlugField()
#     description = serializers.CharField(max_length = 255)
#     point = serializers.CharField(max_length = 255)
#     quantity = serializers.CharField()
#     thumbimage = serializers.ImageField()
#     image = serializers.ImageField()
#     discount = serializers.CharField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Product.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        slug = serializers.SlugRelatedField(
            many=True, read_only=True, slug_field="name"
        )

        fields = [
            "id",
            "category",
            "name",
            "rate",
            "price",
            "discount",
            "brand",
            "code",
            "point",
            "quantity",
            "thumbimage",
            "image",
            "description",
            "slug",
        ]
