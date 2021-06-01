from django.shortcuts import render

# Create your views here.

content ={
    'home_title': 'Магазин',
    'contacts_title': 'Контакты',
    'products_title': ' Каталог',
    'menu_first_item': 'ДОМОЙ',
    'menu_second_item': 'ПРОДУКТЫ',
    'menu_third_item': 'КОНТАКТЫ'
}

def main(request):
    return render(request, 'mainapp/index.html', content)
    

def products(request):
    return render(request, 'mainapp/products.html', content)
    

def contact(request):
    return render(request, 'mainapp/contact.html', content)