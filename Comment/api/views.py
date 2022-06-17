from Comment.models import Books, Comment
from requests import request
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from .permission import IsAdminUserOrReadOnly, IsAuthenticatedOrReadOnly
from .serializer import BooksSerializer, CommentSerializer


class BooksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Books.bookobjects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BooksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        # path("api/books/<int:book_pk>/comments") # comment have relationship with Books
        book_pk = self.kwargs.get("book_pk")  # get id from link
        book = get_object_or_404(Books, pk=book_pk)
        commenter = self.request.user
        comments = Comment.objects.filter(book=book, commenter=commenter)
        if comments.exists():
            raise ValidationError("You have already commented this book")
        serializer.save(book=book, commenter=commenter)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
