from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #print(f'has_permission {request.user.is_authenticated=}')
        # Authenticated users only can see list view
        if request.user.is_authenticated: 
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        #print(f'has_permission {request.method=}')
        # Read permissions are allowed to any request so we'll always 
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        #print(f'{obj.author=} {request.user=} {(obj.author == request.user)=}')
        return obj.author == request.user
