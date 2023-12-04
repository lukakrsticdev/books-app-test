from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import MyBooks
from .serializers import MyBooksSerializer

class MyBooksApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        books = MyBooks.objects.filter(user = request.user.id)
        serializer = MyBooksSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'user': request.user.id
        }
        serializer = MyBooksSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class MyBooksDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_book(self, book_id, user_id):
        try:
            return MyBooks.objects.get(id = book_id, user_id = user_id)
        except MyBooks.DoesNotExist:
            return None
        
    def get(self, request, book_id, *args, **kwargs):
        book = self.get_book(book_id, request.user.id)
        if not book:
            return Response(
                {"res": "Book doesn't exist"},
                status = status.HTTP_404_NOT_FOUND
            )
        
        serializer = MyBooksSerializer(book)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, book_id, *args, **kwargs):
        book = self.get_book(book_id, request.user.id)
        if not book:
            return Response(
                { "message": "Book doesn't exist" },
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = request.data
        serializer = MyBooksSerializer(book, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id, *args, **kwargs):
        book = self.get_book(book_id, request.user.id)
        if not book:
            return Response(
                { "message": "Book doesn't exist" },
                status = status.HTTP_404_NOT_FOUND
            )
        
        book.delete()
        return Response(
            { "message": "Book deleted!" }, 
            status = status.HTTP_200_OK
        )