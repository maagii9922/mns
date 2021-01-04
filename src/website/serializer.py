from django.db.models import fields
from rest_framework import serializers
from src.website.models import (
    Banner,
    Influencer,
    MonthlyProduct,
    SaleProduct,
    btn,
    introductionOne,
)


class bntSerializer(serializers.ModelSerializer):
    class Meta:
        model = btn
        depth = 0
        fields = ["content", "color"]


class BannerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    class Meta:
        model = Banner
        depth = 1
        fields = ["image"]


class IntroductionOneSerialier(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.photo.url if obj.photo else None

    class Meta:
        model = introductionOne
        depth = 0
        fields = "__all__"


class MonthlyProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    class Meta:
        model = MonthlyProduct
        depth = 0
        fields = "__all__"


class SaleProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    class Meta:
        model = SaleProduct
        depth = 0
        fields = "__all__"


class InfluencerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    class Meta:
        model = Influencer
        depth = 0
        fields = "__all__"
