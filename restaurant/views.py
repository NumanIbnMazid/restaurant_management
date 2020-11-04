from django.http import request
from account_management.models import HotelStaffInformation, UserAccount
from account_management.serializers import StaffInfoSerializer
from account_management import serializers
from drf_yasg2.utils import get_serializer_class
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import Serializer
from restaurant.models import Food, FoodCategory, FoodExtra, FoodOption, FoodOptionExtraType, FoodOrder, Restaurant, Table
from utils.response_wrapper import ResponseWrapper
from rest_framework import permissions, status, viewsets
from .serializers import FoodCategorySerializer, FoodDetailSerializer, FoodExtraSerializer, FoodOptionExtraTypeSerializer, FoodOptionSerializer, FoodOrderSerializer, FoodSerializer, RestaurantSerializer, RestaurantContactPerson, RestaurantUpdateSerialier, TableSerializer
from django.db.models import Q
from utils.custom_viewset import CustomViewSet


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    lookup_field = 'pk'
    # serializer_class = RestaurantContactPerson

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = RestaurantSerializer
        elif self.action == 'update':
            self.serializer_class = RestaurantUpdateSerialier
        else:
            self.serializer_class = RestaurantSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action in ["create", 'destroy', 'list']:
            permission_classes = [permissions.IsAdminUser]
        if self.action in ['update', 'restaurant_under_owner']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseWrapper(data=serializer.data, msg='created')
        else:
            return ResponseWrapper(error_code=400, error_msg=serializer.errors, msg='failed to create restaurent')

    def retrieve(self, request, pk, *args, **kwargs):
        qs = Restaurant.objects.filter(pk=pk).first()
        if qs:
            serializer = RestaurantSerializer(instance=qs)
            return ResponseWrapper(data=serializer.data)
        else:
            return ResponseWrapper(error_msg='invalid restaurant id', error_code=400)

    def update(self, request, pk, *args, **kwargs):
        if not (
            self.request.user.is_staff or HotelStaffInformation.objects.filter(
                Q(is_owner=True) | Q(is_manager=True),
                user_id=request.user.pk, restaurant_id=pk
            )
        ):
            return ResponseWrapper(error_code=status.HTTP_401_UNAUTHORIZED, error_msg="can't update please consult with manager or owner of the hotel")
        serializer = RestaurantUpdateSerialier(data=request.data, partial=True)
        if not serializer.is_valid():
            return ResponseWrapper(error_code=400, error_msg=serializer.errors)
        qs = Restaurant.objects.filter(pk=pk)
        if not qs:
            return ResponseWrapper(error_code=404, error_msg=[{"restaurant_id": "restaurant not found"}])

        qs = serializer.update(qs.first(), serializer.validated_data)
        if not qs:
            return ResponseWrapper(error_code=404, error_msg=['update failed'])

        restaurant_serializer = RestaurantSerializer(instance=qs)
        return ResponseWrapper(data=restaurant_serializer.data, msg='updated')

    def restaurant_under_owner(self, request, *args, **kwargs):
        owner_qs = UserAccount.objects.filter(pk=request.user.pk).first()
        restaurant_list = owner_qs.hotel_staff.values_list(
            'restaurant', flat=True)
        qs = Restaurant.objects.filter(pk__in=restaurant_list)
        serializer = RestaurantSerializer(instance=qs, many=True)
        return ResponseWrapper(data=serializer.data)

    def list(self, request, *args, **kwargs):
        qs = Restaurant.objects.all()
        serializer = RestaurantSerializer(instance=qs, many=True)
        return ResponseWrapper(data=serializer.data)


# class FoodCategoryViewSet(viewsets.GenericViewSet):
#     serializer_class = FoodCategorySerializer
#     permission_classes = [permissions.IsAdminUser]
#     queryset = FoodCategory.objects.all()
#     lookup_field = 'pk'

#     def list(self, request):
#         qs = self.get_queryset()
#         serializer = self.serializer_class(instance=qs, many=True)
#         # serializer.is_valid()
#         return ResponseWrapper(data=serializer.data, msg='success')

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             qs = serializer.save()
#             serializer = self.serializer_class(instance=qs)
#             return ResponseWrapper(data=serializer.data, msg='created')
#         else:
#             return ResponseWrapper(error_msg=serializer.errors, error_code=400)

#     def update(self, request, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             qs = serializer.update(instance=self.get_object(
#             ), validated_data=serializer.validated_data)
#             serializer = self.serializer_class(instance=qs)
#             return ResponseWrapper(data=serializer.data)
#         else:
#             return ResponseWrapper(error_msg=serializer.errors, error_code=400)

#     def destroy(self, request, **kwargs):
#         qs = self.queryset.filter(**kwargs).first()
#         if qs:
#             qs.delete()
#             return ResponseWrapper(status=200, msg='deleted')
#         else:
#             return ResponseWrapper(error_msg="failed to delete", error_code=400)


class FoodCategoryViewSet(CustomViewSet):
    serializer_class = FoodCategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = FoodCategory.objects.all()
    lookup_field = 'pk'


class FoodOptionExtraTypeViewSet(CustomViewSet):
    serializer_class = FoodOptionExtraTypeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = FoodOptionExtraType.objects.all()
    lookup_field = 'pk'


class FoodExtraViewSet(CustomViewSet):
    serializer_class = FoodExtraSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = FoodExtra.objects.all()
    lookup_field = 'pk'


class FoodOptionViewSet(CustomViewSet):
    serializer_class = FoodOptionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = FoodOption.objects.all()
    lookup_field = 'pk'


class TableViewSet(CustomViewSet):
    serializer_class = TableSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Table.objects.all()
    lookup_field = 'pk'


class FoodOrderViewSet(CustomViewSet):
    serializer_class = FoodOrderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = FoodOrder.objects.all()
    lookup_field = 'pk'


class FoodViewSet(CustomViewSet):
    serializer_class = FoodSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Food.objects.all()
    lookup_field = 'pk'
    http_method_names = ['post', 'patch', 'put']


class FoodByRestaurantViewSet(CustomViewSet):
    serializer_class = FoodDetailSerializer
    # queryset = Food.objects.all()

    # permission_classes = [permissions.IsAuthenticated]
    # http_method_names = ['get']

    def list(self, request, **kwargs):
        qs = Food.objects.filter(**kwargs)
        serializer = self.serializer_class(instance=qs, many=True)
        return ResponseWrapper(data=serializer.data)
