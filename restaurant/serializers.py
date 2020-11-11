import decimal
from account_management.serializers import StaffInfoGetSerializer
from os import read
from django.db.models.fields.related import RelatedField
from account_management.models import HotelStaffInformation, UserManager
from utils.response_wrapper import ResponseWrapper
from django.db.models import fields

from .models import *
from django.db.models import Q, query_utils, Min
from rest_framework import serializers


class FoodOptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOptionType
        fields = '__all__'


class FoodExtraTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodExtraType
        fields = '__all__'


class FoodExtraSerializer(serializers.ModelSerializer):
    extra_type = FoodExtraTypeSerializer(read_only=True)

    class Meta:
        model = FoodExtra
        fields = '__all__'


class GroupByListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        return {
            extra_type.name: super(GroupByListSerializer, self).to_representation(
                FoodExtra.objects.filter(extra_type=extra_type, pk__in=list(data.values_list('id', flat=True))))
            for extra_type in FoodExtraType.objects.filter(pk__in=list(data.values_list('extra_type_id', flat=True)))
        }


class FoodExtraGroupByTypeSerializer(serializers.ModelSerializer):
    # extra_type = FoodExtraTypeSerializer(read_only=True)

    class Meta:
        model = FoodExtra
        fields = ['id', 'name', 'price']
        list_serializer_class = GroupByListSerializer


class FoodExtraPostPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodExtra
        fields = '__all__'


class FoodExtraTypeDetailSerializer(serializers.ModelSerializer):
    extra_type = FoodExtraTypeSerializer(read_only=True)

    class Meta:
        model = FoodExtra
        fields = '__all__'

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'


class FoodOptionSerializer(serializers.ModelSerializer):
    option_type = FoodOptionTypeSerializer(read_only=True)

    class Meta:
        model = FoodOption
        fields = '__all__'


class FoodOptionBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOption
        fields = '__all__'


"""
class FoodOptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOptionType
        fields = '__all__'
"""


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    staff_assigned = StaffInfoGetSerializer(read_only=True, many=True)

    class Meta:
        model = Table
        fields = '__all__'


class StaffIdListSerializer(serializers.Serializer):
    staff_list = serializers.ListSerializer(child=serializers.IntegerField())


class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = '__all__'


class OrderedItemUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        # fields = '__all__'
        exclude = ['status']



class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrder
        fields = '__all__'


class FoodOrderForStaffSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    price_dict = serializers.SerializerMethodField()

    class Meta:
        model = FoodOrder
        fields = ['id',
                  "remarks",
                  "table",
                  "status",
                  "price_dict"
                  ]

    # def get_status(self, obj):
    #     return obj.get_status_display()
    def get_price_dict(self, obj):
        ordered_items_qs = obj.ordered_items.exclude(
            status__in=["5_PAID", "6_CANCELLED", "0_ORDER_INITIALIZED"])

        food_price = decimal.Decimal(0.0)
        tax_amount = decimal.Decimal(0.0)
        total_price = decimal.Decimal(0.0)
        service_charge = decimal.Decimal(0.0)
        for ordered_item in ordered_items_qs:
            item_price = ordered_item.quantity*ordered_item.food_option.price
            extra_price = ordered_item.quantity * sum(
                list(
                    ordered_item.food_extra.values_list('price', flat=True)
                )
            )
            food_price += item_price+extra_price
        total_price += food_price
        if obj.table.restaurant.service_charge_is_percentage:
            service_charge = total_price * obj.table.restaurant.service_charge/100
        else:
            service_charge = total_price + obj.table.restaurant.service_charge
        total_price += service_charge
        tax_amount = total_price * obj.table.restaurant.tax_percentage/100
        total_price += tax_amount
        return {"total_price": total_price, "tax_amount": tax_amount, "service_charge": service_charge}


class FoodOrderUserPostSerializer(serializers.ModelSerializer):
    ordered_items = OrderedItemSerializer(
        many=True, read_only=True, required=False)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = FoodOrder
        fields = ['ordered_items', 'table', 'remarks', 'status', 'id']


class AddItemsSerializer(serializers.Serializer):
    ordered_items = OrderedItemUserPostSerializer(
        many=True, required=True)


class FoodSerializer(serializers.ModelSerializer):
    category = FoodCategorySerializer(read_only=True)

    class Meta:
        model = Food
        fields = '__all__'


class FoodWithPriceSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Food
        fields = [
            "name",
            "image",
            "description",
            "restaurant",
            "is_top",
            "is_recommended",
            'price',
            'ingredients',
            'category',
            'id'
        ]

    def get_price(self, obj):
        option_qs = obj.food_options.order_by('price').first()
        if option_qs:
            return option_qs.price
        else:
            return None


class FoodsByCategorySerializer(serializers.ModelSerializer):
    foods = FoodWithPriceSerializer(many=True)

    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'image', 'foods']


class FoodDetailSerializer(serializers.ModelSerializer):
    category = FoodCategorySerializer(read_only=True)
    food_extras = FoodExtraGroupByTypeSerializer(read_only=True, many=True)
    food_options = FoodOptionSerializer(read_only=True, many=True)
    price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Food
        fields = [
            'id',
            "name",
            "image",
            "description",
            "restaurant",
            "category",
            "is_top",
            "is_recommended",
            "food_extras",
            "food_options",
            'ingredients',
            'price',
        ]

    def get_price(self, obj):
        option_qs = obj.food_options.order_by('price').first()
        if option_qs:
            return option_qs.price
        else:
            return None


class RestaurantUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ['status', 'subscription', 'subscription_ends']


class RestaurantContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantContactPerson
        fields = '__all__'



class HotelStaffInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelStaffInformation
        fields = '__all__'


class TableStaffSerializer(serializers.ModelSerializer):
    quantity_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = FoodOrder
        fields = '__all__'

    def get_quantity_list(self, obj):
        if obj.is_occupied:
            quantity_qs = obj.ordered_items.exclude(
                status__in=["5_PAID", "6_CANCELLED"]).order_by('-id').first()
            # item_qs = OrderedItem.objects.filter(food_order=order_qs)
            if not quantity_qs:
                return {}
            serializer = OrderedItemSerializer(quantity_qs)
            temp_data_dict = serializer.data
            return temp_data_dict


    quantity_list = QuantitySerializer(read_only=True, many= True)
    order_info = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Table
        fields = ['quantity_list','table_no', 'restaurant',
                  'is_occupied', 'name', 'order_info', 'id']

    def get_order_info(self, obj):
        if obj.is_occupied:
            order_qs = obj.food_orders.exclude(
                status__in=["5_PAID", "6_CANCELLED"]).order_by('-id').first()
            # item_qs = OrderedItem.objects.filter(food_order=order_qs)
            if not order_qs:
                return {}
            serializer = FoodOrderForStaffSerializer(order_qs)
            temp_data_dict = serializer.data
            price_dict = temp_data_dict.pop('price_dict', {})
            temp_data_dict.update(price_dict)
            # temp_data_dict['total_price'] = 380
            return temp_data_dict
        else:
            return {}
