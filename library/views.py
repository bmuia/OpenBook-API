from rest_framework import generics, views
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .serializers import BookSerializer
from .models import Book
import math

class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SimplePaginatedBooksView(APIView):

    def get(self, request):

        pg = int(request.GET.get("pg", 1))
        limit = int(request.GET.get("limit", 20))

  
        books = Book.objects.all().order_by("id")
        total_items = books.count()
        total_pages = math.ceil(total_items / limit) if total_items > 0 else 1


        start = (pg - 1) * limit
        end = start + limit
        paginated_books = books[start:end]

        serializer = BookSerializer(paginated_books, many=True)

        next_pg = pg + 1 if pg < total_pages else None
        prev_pg = pg - 1 if pg > 1 else None

        return Response({
            "page": pg,
            "limit": limit,
            "total_items": total_items,
            "total_pages": total_pages,
            "next_page": next_pg,
            "previous_page": prev_pg,
            "results": serializer.data
        })



