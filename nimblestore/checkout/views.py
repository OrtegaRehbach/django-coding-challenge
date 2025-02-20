from django.http.response import JsonResponse
from django.views import generic
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class IndexView(generic.TemplateView):
    template_name = "index.html"


class ProductListView(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be listed.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(APIView):
    parser_classes = (JSONParser,)
    authentication_classes = []

    def post(self, request):
        """
        API endpoint that calculates the order total.
        """
        response_obj = {"total": 0}

        order_items = request.data
        total = 0
        error_messages = []

        for item in order_items:
            product_name = item.get("name")
            quantity_requested = item.get("quantity", 0)

            # Check if the product exists
            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                error_messages.append(f"Product '{product_name}' does not exist.")
                continue

            # Check that there is enough stock
            if product.quantity < quantity_requested:
                error_messages.append(
                    f"Product '{product.name}' does not have enough stock. Current stock: {product.quantity}."
                )
                continue

            # Add to the total
            total += product.price * quantity_requested

        if error_messages:
            return JsonResponse({"errors": error_messages}, status=400)

        response_obj["total"] = total

        return JsonResponse(response_obj, safe=False)
