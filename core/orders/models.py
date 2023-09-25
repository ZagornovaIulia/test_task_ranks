from django.db import models
from items.models import Item
from django.urls import reverse



class Order(models.Model):
    first_name = models.CharField("Имя", max_length=60)
    last_name = models.CharField("Фамилия", max_length=60)
    email = models.EmailField("Электронная почта")
    address = models.CharField("Адрес", max_length=150)
    postal_code = models.CharField("Почтовый индекс", max_length=30)
    city = models.CharField("Город", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField("Оплачено", default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f'Order Item {self.id}'

    def get_cost(self):
        return self.price * self.quantity



