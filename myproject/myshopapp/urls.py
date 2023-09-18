from django.urls import path
from myshopapp.views import products, AddProduct, ProductPage


app_name = 'myshopapp'

urlpatterns = [
    path('products/', products, name='products'),
    path('product/', AddProduct.as_view(), name='add_product'),
    # path('product_page/<int:pk>', ProductPage.as_view(), name='product_page'),
]
