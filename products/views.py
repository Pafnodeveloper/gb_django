from django.shortcuts import render
import json


# Create your views here.


def index(request):
    context = {"title": "GeekShop"}
    return render(request, 'products\\index.html', context)


def products(request):
    # toJSON = {
    #   "title": "GeekShop - Каталог",
    #   "products" :
    #           [
    #             {
    #               "name": "Худи черного цвета с монограммами adidas Originals",
    #               "price": "6 090,00 руб.",
    #               "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
    #                 "img": "vendor/img/products/Adidas-hoodie.png",
    #                 "isAvailable": True
    #             },
    #
    #             {
    #               "name": "Синяя куртка The North Face",
    #               "price": "23 725,00 руб.",
    #               "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
    #                 "img": "vendor/img/products/Blue-jacket-The-North-Face.png",
    #                 "isAvailable": False
    #             },
    #
    #             {
    #               "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
    #               "price": "3 390,00 руб.",
    #               "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
    #                 "img": "vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
    #                 "isAvailable": True
    #             },
    #
    #             {
    #               "name": "Черный рюкзак Nike Heritage",
    #               "price": "2 340,00 руб.",
    #               "description": "Плотная ткань. Легкий материал.",
    #                 "img": "vendor/img/products/Black-Nike-Heritage-backpack.png",
    #                 "isAvailable": True
    #             },
    #
    #             {
    #               "name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
    #               "price": "13 590,00 руб.",
    #               "description": "Гладкий кожаный верх. Натуральный материал.",
    #                 "img": "vendor/img/products/Black-Dr-Martens-shoes.png",
    #                 "isAvailable": True
    #             },
    #
    #             {
    #               "name": "Темно-синие широкие строгие брюки ASOS DESIGN",
    #               "price": "2 890,00 руб.",
    #               "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
    #                 "img": "vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
    #                 "isAvailable": True
    #             }
    #
    #           ]
    # }
    # end_file = open("products.json", 'w')
    # json.dump(toJSON, end_file)
    # end_file.close()

    context = {}

    with open('products\\fixtures\products.json') as file:
        for product in file:
            context.update(json.loads(product))
    print(context.items())
    return render(request, 'products\\products.html', context)
