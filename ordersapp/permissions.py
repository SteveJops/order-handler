from rest_framework import permissions


class IsStatusNotNewOrRefusalDoNotUpdate(permissions.BasePermission):
    """
    Class with custom permissions
    """

    def has_object_permission(self, request, view, obj):
        """
        Method for creating a permission to update order if order`s status is either New nor Refusal
        """

        if (
            request.method == "PUT"
            and obj.status == "New"
            or request.method == "PUT"
            and obj.status == "Refusal"
        ):
            return True
