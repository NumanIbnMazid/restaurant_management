from django.db.models import Q
from restaurant.models import Restaurant
from account_management.models import HotelStaffInformation
from rest_framework import permissions

"""
[summary]
        # self.check_object_permissions(request, obj=Restaurant.objects.get(pk=1))

Returns
-------
[type]
    [description]
"""


class IsRestaurantOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Not a restaurant owner.'

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            user=request.user, is_owner=True)
        if hotel_staff_qs:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            restaurant=obj.pk, user=request.user, is_owner=True)
        if hotel_staff_qs:
            return True
        else:
            return False


class IsRestaurantManager(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Not a restaurant manager.'

    # def has_permission(self, request, view):
    #     """
    #     Return `True` if permission is granted, `False` otherwise.
    #     """

    #     return False
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            user=request.user, is_manager=True)
        if hotel_staff_qs:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            restaurant=obj, user_id=request.user.pk, is_manager=True)
        if hotel_staff_qs:
            return True
        else:
            return False


class IsRestaurantWaiter(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Not a restaurant waiter.'

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            user=request.user, is_waiter=True)
        if hotel_staff_qs:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            restaurant=obj.pk, user=request.user, is_waiter=True)
        if hotel_staff_qs:
            return True
        else:
            return False


class IsRestaurantStaff(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Not a restaurant staff.'

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            Q(user=request.user), Q(is_waiter=True) | Q(is_owner=True) | Q(is_manager=True))
        if hotel_staff_qs:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # hotel_staff_qs = HotelStaffInformation.objects.filter(
        #     restaurant=obj.pk, user=request.user, is_waiter=True)
        hotel_staff_qs = HotelStaffInformation.objects.filter(
            Q(user=request.user, restaurant=obj.pk), Q(is_waiter=True) | Q(is_owner=True) | Q(is_manager=True))

        if hotel_staff_qs:
            return True
        else:
            return False
