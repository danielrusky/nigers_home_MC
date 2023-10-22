from django.shortcuts import render

from catalog.models import Product, Contacts, Category


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


def product(request, pk):
    return render(request, 'catalog/product.html', {'product': Product.objects.get(pk=pk)})

# def home(request):
#     return render(request, 'catalog/home.html')
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'(У вас новое сообщение от: {name} (телефон: {phone}): {message}')
#         return render(request, 'catalog/contacts.html')
