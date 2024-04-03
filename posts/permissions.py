from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # auth user sees LIST VIEW only
        if request.user.is_authenticated:
            return True
        return False
    
    
    def has_object_permission(self, request, view, obj):
    # verification for auth user 
        if request.method in permissions.SAFE_METHODS:
            return True
    
    # if author is verified, author can edit/delete his post(s)
        return obj.author == request.user