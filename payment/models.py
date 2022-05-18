from django.db import models


class Item(models.Model):
	USD = 'USD'
	RUB = 'RUB'

	CURRENCY_CHOICE = [
		(USD, 'Доллар'),
		(RUB, 'Рубль')
	]

	name = models.CharField(verbose_name="Наименование", max_length=255)
	description = models.TextField(verbose_name="Описание", max_length=255, blank=True)
	price = models.IntegerField(verbose_name="Цена")
	price_id = models.CharField(verbose_name="ID Цены", max_length=255, blank=True, null=True)
	currency = models.CharField(verbose_name="Валюта", choices=CURRENCY_CHOICE, max_length=255)

	def __str__(self):
		return str(self.name)


class Discount(models.Model):
	name = models.CharField(verbose_name="Наименование купона", max_length=255)
	discount_id = models.CharField(verbose_name="ID купона", max_length=255)

	def __str__(self):
		return str(self.name)


class Tax(models.Model):
	SALES = 'Sales tax'
	VAT = 'VAT'

	TAX_CHOICE = [
		(SALES, 'Налог с продажи'),
		(VAT, 'НДС'),
	]

	type = models.CharField(verbose_name="Тип налога", max_length=255, choices=TAX_CHOICE)
	description = models.CharField(verbose_name="Описание налога", blank=True, max_length=255)
	tax_rate_id = models.CharField(verbose_name="ID налога", max_length=255)

	def __str__(self):
		return str(self.type.label)


class Order(models.Model):
	items = models.ManyToManyField(Item, verbose_name="Товары")
	discount = models.ForeignKey(Discount, on_delete=models.CASCADE, verbose_name="Скидка")
	tax = models.ForeignKey(Tax, on_delete=models.CASCADE, verbose_name="Налог")

	def __str__(self):
		return f'Заказ №{self.id} - {self.items.count()} шт'
