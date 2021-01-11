from rest_framework import permissions

class permissionsUsers(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user == obj.author:
            return True
        
        if request.user.id != 1:
            return False
