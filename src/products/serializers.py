from rest_framework import serializers
from src.products.models import Category, Product

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

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    # catname = serializers.CharField(source='category.catname')
    # catname_en = serializers.CharField(source='category.catname_en')
    category_catname = serializers.RelatedField(source='category', read_only=True)
    # category_name_en = serializers.RelatedField(source='category', read_only=True)
    category_catname_en = serializers.RelatedField(source='category', read_only=True)

    class Meta:
        depth = 1
        model = Product
        slug = serializers.SlugRelatedField(
            many=True, read_only=True, slug_field="name"
        )

        fields = [
            "id",
            "category_catname",
            "category_catname_en",
            "name",
            "name_en",
            "rate",
            "price",
            "discount",
            "brand",
            "brand_en",
            "code",
            "point",
            "quantity",
            "thumbimage",
            "image",
            "description",
            "description_en",
            "slug",
            "link_to_emonos",
        ]

