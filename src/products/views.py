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
from rest_framework.pagination import PageNumberPagination

@api_view(["GET"])
@permission_classes([])
def category_list(request,category):
    """
    List all code products, or create a new snippet.
    """
    if request.method == "GET":
        paginator = PageNumberPagination()
        # paginator.page_size = 1
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        products = Product.objects.filter(category=category)
        result_page = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(result_page, many=True)
        # serializer = ProductSerializer(products, many=True)
       
        return Response(serializer.data)





@api_view(["GET"])
@permission_classes([])
def product_list(request):
    """
    List all code products, or create a new snippet.
    """
    if request.method == "GET":
        paginator = PageNumberPagination()
        # paginator.page_size = 1
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        products = Product.objects.all()
        result_page = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(result_page, many=True)
        # serializer = ProductSerializer(products, many=True)
       
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
        return Response({
            "en": {
                "id": serializer.data.get('id'),
                "category": serializer.data.get('category'),
                "category_en": serializer.data.get('category_en'),
                "name": serializer.data.get('name_en'),
                "rate": serializer.data.get('rate'),
                "price": serializer.data.get('price'),
                "discount": serializer.data.get('discount'),
                "brand": serializer.data.get('brand'),
                "brand_en": serializer.data.get('brand_en'),
                "code": serializer.data.get('code'),
                "point": serializer.data.get('point'),
                "quantity": serializer.data.get('quantity'),
                "thumbimage": serializer.data.get('thumbimage'),
                "image": serializer.data.get('image'),
                "description_en": serializer.data.get('description_en'),
                "slug": serializer.data.get('slug'),
                "link_to_emonos": serializer.data.get('link_to_emonos')
            },
            "mn":{
                "id": serializer.data.get('id'),
                "category": serializer.data.get('category'),
                "name": serializer.data.get('name'),
                "rate": serializer.data.get('rate'),
                "price": serializer.data.get('price'),
                "discount": serializer.data.get('discount'),
                "brand": serializer.data.get('brand'),
                "code": serializer.data.get('code'),
                "point": serializer.data.get('point'),
                "quantity": serializer.data.get('quantity'),
                "thumbimage": serializer.data.get('thumbimage'),
                "image": serializer.data.get('image'),
                "description": serializer.data.get('description'),
                "slug": serializer.data.get('slug'),
                "link_to_emonos": serializer.data.get('link_to_emonos')
            }
        })


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
    phone = request.data["phone"]
    fd = Feedback.objects.create(name=name, email=email, message=message, phone=phone)
    fd.save()
    return Response({"result": "ok"})