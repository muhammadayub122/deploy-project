from api.views.user_list import UserModelViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter



r = DefaultRouter()

r.register(r'users', UserModelViewSet, basename='users')


urlpatterns = [
    path('', include(r.urls)),
]
