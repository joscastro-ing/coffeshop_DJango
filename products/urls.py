from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPI

urlpatterns = [
    path('', ProductListView.as_view(), name='list_product'),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
    path('api/', ProductListAPI.as_view(), name='list_product_api'),
] 