from Comment.models import Books, Comment
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .serializer import BooksSerializer, CommentSerializer


class BooksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Books.bookobjects.all()
    serializer_class = BooksSerializer


class BooksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # path("api/books/<int:book_pk>/comments") # comment have relationship with Books
        book_pk = self.kwargs.get("kitap_pk")  # get id from link
        book = get_object_or_404(Books, pk=book_pk)
        serializer.save(book=book)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
