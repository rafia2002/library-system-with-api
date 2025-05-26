from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookApiView

router = DefaultRouter()
router.register(r'Books', BookApiView, basename='book')

urlpatterns = [
    path('',include(router.urls)),
]