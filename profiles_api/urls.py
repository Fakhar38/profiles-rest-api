from django.urls import path, include
from rest_framework import routers
from .views import HelloApiView, HelloApiViewset

app_name = 'profiles_api'


router = routers.DefaultRouter()
router.register('hello-viewset', HelloApiViewset, base_name='hello-viewset')

urlpatterns = [
    path('hello-api-view/', HelloApiView.as_view()),
    path('', include(router.urls)),
]
