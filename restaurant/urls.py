# from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import include, path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('food_option_extra_type', FoodOptionExtraTypeViewSet,
                basename="food_option_extra_type")
router.register('food_category', FoodCategoryViewSet,
                basename="food_category")

router.register('food_extra', FoodExtraViewSet,
                basename="food_extra")

router.register('food_option', FoodOptionViewSet,
                basename="food_option")

router.register('table', TableViewSet,
                basename="table")

router.register('food', FoodViewSet,
                basename="food")

urlpatterns = [
    path('', include(router.urls)),
    path('restaurant/',
         RestaurantViewSet.as_view({'post': 'create', 'get': 'list'}), name='restaurant_create_and_list'),
    path('restaurant/<int:pk>/',
         RestaurantViewSet.as_view({'patch': 'update', 'get': 'retrieve'}), name='restaurant_update'),
    path("food_category/",
         FoodCategoryViewSet.as_view({"post": "create", "get": "list"})),
    path("food_category/<int:pk>/",
         FoodCategoryViewSet.as_view({"patch": "update", "delete": "destroy"})),

    path('restaurant_under_owner/',
         RestaurantViewSet.as_view({'get': 'restaurant_under_owner'}), name='restaurant_under_owner'),
]
