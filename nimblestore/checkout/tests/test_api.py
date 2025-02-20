import os

import django
import pytest
from checkout.models import Product
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nimblestore.settings")
django.setup()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_product():
    def _create_product(name, price, quantity):
        return Product.objects.create(name=name, price=price, quantity=quantity)

    return _create_product


def dummy_test():
    assert 1 == 1


def dummy_failing():
    assert 1 == 2


@pytest.mark.django_db
def test_get_products(api_client, create_product):
    """
    Test to get the general list of products.
    """
    create_product(name="Test Product 1", price=10.00, quantity=100)
    create_product(name="Test Product 2", price=15.00, quantity=200)

    url = reverse("product-list")  # Adjust this to your actual URL name
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
def test_post_order(api_client, create_product):
    """
    Test that sends an order and verifies the obtained total.
    """
    product1 = create_product(name="Test Product 1", price=10.00, quantity=100)
    product2 = create_product(name="Test Product 2", price=15.00, quantity=200)

    url = reverse("order")

    order_data = [
        {"name": product1.name, "quantity": 2},  # 2 * 10.00 = 20.00
        {"name": product2.name, "quantity": 1},  # 1 * 15.00 = 15.00
    ]

    response = api_client.post(url, order_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert "total" in response_json
    assert response_json["total"] == "35.00"


@pytest.mark.django_db
def test_put_product(api_client, create_product):
    """
    Test to update the data of a product using the PUT method.
    """
    product = create_product(name="Old Name", price=20.00, quantity=50)
    url = reverse("product-list") + f"{product.id}/"

    updated_data = {
        "name": "New Name",
        "price": 25.00,
        "quantity": 75,
    }

    response = api_client.put(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    product.refresh_from_db()
    assert product.name == "New Name"
    assert product.price == 25.00
    assert product.quantity == 75


@pytest.mark.django_db
def test_patch_product(api_client, create_product):
    """
    Test to partially update the data of a product using the PATCH method.
    """
    product = create_product(name="Partial Update", price=30.00, quantity=80)
    url = reverse("product-list") + f"{product.id}/"

    updated_data = {
        "price": 35.00,  # Change the price from 30.00 to 35.00
    }

    response = api_client.patch(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    product.refresh_from_db()
    assert product.price == 35.00  # Only the price value should be different
    assert product.name == "Partial Update"
    assert product.quantity == 80
