from django.shortcuts import render


def main(request):
    return render(request, 'menu/index.html')


def menu_item_view(request, slug):
    return render(request, 'menu/index.html')
