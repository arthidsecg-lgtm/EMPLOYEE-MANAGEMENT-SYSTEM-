from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, UserViewSet

# urlpatterns = [
#     path('departments/',DepartmentViewSet),
#     path('employee/',EmployeeViewSet),
#     path('users/',UserViewSet),
# ]





router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

