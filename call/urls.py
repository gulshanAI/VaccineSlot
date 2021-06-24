from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('', views.RegisterForVaccine, basename='RegisterForVaccine')

urlpatterns = [
    path('', views.vaccineApi),
    path('registerForVaccine', include(router.urls)),
]
