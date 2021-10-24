from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from baskets.models import Basket
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required()
def basket_add(request, product_id):
    # get product from DB by his id
    product = Product.objects.get(id=product_id)
    # get QuerySet of baskets
    baskets = Basket.objects.filter(user=request.user, product=product)

    # если QuerySet пустой
    if not baskets.exists():
        # создаем объект типа "корзина"
        Basket.objects.create(user=request.user, product=product, quantity=1)
        # перенаправляем на страницу, где было произведено действие
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        # вычленяем из сета элемент
        basket = baskets.first()
        # увеличиваем его количество на один
        basket.quantity += 1
        # сохраняем в БД с новым значением
        basket.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
