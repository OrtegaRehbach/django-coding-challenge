from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IndexView, OrderView, ProductListView

router = DefaultRouter()
router.register(r"products", ProductListView, basename="product")

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("api", IndexView.as_view(), name="index"),
    path("api/order/", OrderView.as_view(), name="order"),
    path("api/", include(router.urls)),
]
