from django.urls import path
from .views import SnippetList, SnippetDetail

urlpatterns = [
    path('task', SnippetList.as_view(), ""),
    path('task/details/<int:pk>', SnippetDetail.as_view(), ""),
]