from django.urls import path
from .views import HelloApiView

app_name = 'profiles_api'

urlpatterns = [
    path('hello-api-view/', HelloApiView.as_view()),
]
