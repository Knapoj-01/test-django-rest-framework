from django.urls import path
from .views import TestReactView
urlpatterns = [
    path('', TestReactView.as_view() ),
]