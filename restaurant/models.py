from os import name, truncate
import restaurant
from django.db import models
from django.db.models import manager

# Create your models here.
"""
    TODO
    food - edit
    table delete - delete
    waiter - delete
    """


class Subscription(models.Model):
    name = models.CharField(max_length=90)
    code = models.CharField(max_length=5, unique=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    RESTAURANT_STATUS = [('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')]

    name = models.CharField(max_length=250)
    logo = models.ImageField(blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=50, decimal_places=45, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=50, decimal_places=45, null=True, blank=True)
    service_charge_is_percentage = models.BooleanField(default=False)
    service_charge = models.DecimalField(
        max_digits=8, decimal_places=2, default=00.00)
    tax_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, default=00.00)
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.URLField(null=True, blank=True)
    status = models.CharField(
        choices=RESTAURANT_STATUS, max_length=25, default="ACTIVE")
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, related_name='restaurants')
    subscription_ends = models.DateField()

    def __str__(self):
        return self.name

class RestaurantContactPerson(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='contact_persons')

    def __str__(self):
        return self.name

class RestaurantPromoCategory(models.Model):
    category_name = models.CharField(max_length=80)

    def __str__(self):
        return self.category_name

class FoodCategory(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='food_category')

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='food')
    category = models.ForeignKey(
        FoodCategory, null=True, blank=True, on_delete=models.PROTECT, related_name='foods')
    # promotion_category = models.ManyToManyField(
    #     RestaurantPromoCategory, blank=True)
    is_top = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FoodOptionExtraType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FoodExtra(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    food = models.ForeignKey(Food, on_delete=models.CASCADE,
                             related_name='food_extras')
    extra_type = models.ForeignKey(
        FoodOptionExtraType, on_delete=models.CASCADE, related_name='food_extras')

    def __str__(self):
        return self.name

class FoodOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='food_options')
    option_type = models.ForeignKey(
        FoodOptionExtraType, on_delete=models.CASCADE, related_name='food_options')

    def __str__(self):
        return self.name

class Table(models.Model):
    table_no = models.IntegerField(null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='tables')
    name = models.CharField(max_length=50, null=True, blank=True)
    staff_assigned = models.ManyToManyField(
        to='account_management.HotelStaffInformation', blank=True)

    def __str__(self):
        return self.name

class FoodOrder(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.SET_NULL, null=True, related_name='food_orders')

    def __str__(self):
        return self.table

class OrderedItem(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    food_option = models.ForeignKey(
        FoodOption, on_delete=models.PROTECT, related_name='ordered_items')
    food_extra = models.ManyToManyField(
        FoodExtra, blank=True, related_name='ordered_items')
    food_order = models.ForeignKey(
        FoodOrder, on_delete=models.CASCADE, related_name='ordered_items')

    def __str__(self):
        return self.amount