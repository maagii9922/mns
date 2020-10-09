from rest_framework import serializers
from src.products.models import Product

class ProductSerializer(serializers.Serializer):
    category = serializers.CharField()
    brand = serializers.CharField()
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    rate = serializers.IntegerField()
    slug = serializers.SlugField()
    description = serializers.CharField(max_length = 255)
    point = serializers.CharField(max_length = 255)
    quantity = serializers.CharField()
    thumbimage = serializers.ImageField()
    image = serializers.ImageField()
    discount = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.category = validated_data.get('category', instance.category)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get('description', instance.description)
        instance.point = validated_data.get('point',instance.point)
        instance.quantity = validated_data.get('quantity',instance.quantity)
        instance.thumbimage = validated_data.get ('thumbimage', instance.thumbimage)
        instance.image = validated_data.get('image', instance.image)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 5
        model = Product
        slug=  serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

        fields = ['category', 'brand', 'name', 'price','slug','description','point','quantity','thumbimage','image', 'discount', 'rate']
