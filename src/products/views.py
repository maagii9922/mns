from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from src.products.models import Product
from src.products.serializers import ProductSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer
import json
from src.website.models import Feedback


@api_view(["GET"])
@permission_classes([])
def product_list(request):
    """
    List all code products, or create a new snippet.
    """
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        with open(
            "/var/www/cosmeticFront/src/data/products.json", "w" , encoding='utf8'
        ) as outfile:
            json.dump(serializer.data, outfile, indent=4, ensure_ascii=False)

        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([])
# def featured_product(request, pk):
#     try:
#         featured = Product.objects.filter()


@api_view(["POST"])
@permission_classes([])
def feedback(request):
    """
    САНАЛ ХҮСЭЛТ ХҮЛЭЭЖ АВАХ
    """
    name = request.data["name"]
    email = request.data["email"]
    message = request.data["message"]
    fd = Feedback.objects.create(name=name, email=email, message=message)
    fd.save()
    return Response({"result": "ok"})