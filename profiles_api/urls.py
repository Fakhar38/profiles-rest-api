from django.urls import path, include
from rest_framework import routers
from profiles_api import views

app_name = 'profiles_api'


router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloApiViewset, base_name='hello-viewset')
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    path('hello-api-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
