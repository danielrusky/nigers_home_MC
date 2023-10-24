from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView, DeleteView

from catalog.models import Product, Contacts, Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description')
    success_url = reverse_lazy('catalog:home')


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class CatalogTemplateView(TemplateView):
    model = Product


def home(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contacts.objects.create(name=name, phone=phone, message=message)
        print(f'У вас новое сообщение от: {name}(телефон:{phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', {'contacts': Contacts.objects.get(pk=1)})


def toggle_active(request, slug):
    products = get_object_or_404(Product, slug=slug)
    if products.to_publish:
        products.to_publish = False
    else:
        products.to_publish = True
    products.save()
    return redirect('catalog:home', slug=products.slug)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['contacts'] = Contacts.objects.get(pk=1)
#         return context
#
#
# class CatalogTemplateView(TemplateView):
#     template_name = 'catalog/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context


# def product(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product_item
#     }
#     return render(request, 'catalog/product.html', {'product': Product.objects.get(pk=pk)})


# def create_category(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         Category.objects.create(name=name, description=description)
#         return redirect('home')
#     return render(request, 'catalog/create_category.html')

# def create_product(request):
#     if request.method == 'POST':
#         category = request.POST.get('product')
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         image = request.FILES.get('image_product')
#         Product.objects.create(name=name, description=description, price=price,
#                                image=image, category=Category.objects.get(id=category))
#         print(f"Данные:\n"
#               f"Название: {name}\n"
#               f"Описание: {description}\n"
#               f"Цена: {price}\n"
#               f"Фото: {image}\n"
#               f"Категория: {category}")
#     return render(request, 'catalog/create_product.html', {'categories': Category.objects.all()})

# def product(request, pk):
#     return render(request, 'catalog/product.html', {'product': Product.objects.get(pk=pk)})
