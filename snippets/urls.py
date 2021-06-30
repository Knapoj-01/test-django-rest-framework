from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetView.as_view()),
    path('snippets/<int:pk>/', views.snippet_detail),
]