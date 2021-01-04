from re import T
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from src.products.models import Product
from src.products.serializers import ProductSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer

from src.website.serializer import (
    BannerSerializer,
    InfluencerSerializer,
    IntroductionOneSerialier,
    MonthlyProductSerializer,
    SaleProductSerializer,
)
from src.website.models import (
    Banner,
    Influencer,
    MonthlyProduct,
    SaleProduct,
    introductionOne,
)
import json

"""
Нүүр Баннер зураг
"""


@api_view(["GET"])
@permission_classes([])
def banner(request):
    if request.method == "GET":
        banner = Banner.objects.all()
        serializer = BannerSerializer(banner, many=True)

        return Response(serializer.data)


"""
Нүүр хуудас эхний танилцуулга
"""


@api_view(["GET"])
@permission_classes([])
def introduction(request):
    if request.method == "GET":
        introduction = introductionOne.objects.all()
        serializer = IntroductionOneSerialier(introduction, many=True)

        return Response(serializer.data)


"""
Сарын хямдралтай бүтээгдэхүүн
"""


@api_view(["GET"])
@permission_classes([])
def monthlyproduct(request):
    if request.method == "GET":
        product = MonthlyProduct.objects.all()
        serializer = MonthlyProductSerializer(product, many=True)

        return Response(serializer.data)


"""
Хямдралтай бүтээгдэхүүн
"""


@api_view(["GET"])
@permission_classes([])
def saleproduct(request):
    if request.method == "GET":
        saleproduct = SaleProduct.objects.all()
        serializer = SaleProductSerializer(saleproduct, many=True)
        return Response(serializer.data)


"""
Нүүр хуудас нөлөөлөгч нар
"""


@api_view(["GET"])
@permission_classes([])
def influencer(request):
    if request.method == "GET":
        influencer = Influencer.objects.all()
        serializer = InfluencerSerializer(influencer, many=True)

        return Response(serializer.data)
