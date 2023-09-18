# from django.shortcuts import render
# from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView

from .forms import ProductForm

from .models import OrderModel, CustomerModel, ProductModel


def products(request):
    all_products = ProductModel().return_all_products()
    all_products_str = ['<br>' + str(i) for i in all_products]

    return HttpResponse(f"<h1>Продукты</h1><br>{all_products_str}")


class AddProduct(CreateView):
    # Модель в которую выполняется сохранение
    model = ProductModel
    # Класс на основе которого будет валидация полей
    form_class = ProductForm
    # Шаблон с помощью которого будут выводиться данные
    template_name = 'myshopapp/add_product.html'
    # На какую страницу  будет перенаправление в случае успешного сохранения формы
    # success_url = '/add_product/'
    # Выведем все существующие записи на странице
    extra_context = {'products': ProductModel.objects.all()}


class ProductPage(DetailView):
    # model = AuthorModel
    # template_name = 'seminar4app/author_page.html'
    pass


class OrderProductsView(ListView):
    model = OrderModel
    template_name = '/seminar3app/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = CustomerModel.objects.get(pk=self.kwargs['pk'])
        orders = OrderModel.objects.filter(customer=customer).all()
        from django.db import connection
        print(connection.queries)
        context['orders'] = orders
        return context
