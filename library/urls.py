from django.urls import path
from .views import ListBooksView, SimplePaginatedBooksView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('books/paginated/', SimplePaginatedBooksView.as_view(), name='paginated-books'),
]
