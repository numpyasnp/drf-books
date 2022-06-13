from django.urls import path

from . import views as api_views

urlpatterns = [
    path("books", api_views.BooksListCreateAPIView.as_view(), name="books-list"),
    path("books/<int:pk>", api_views.BooksDetailAPIView.as_view(), name="books-detail"),
    path(
        "books/<int:book_pk>/comments",
        api_views.CommentCreateAPIView.as_view(),
        name="comments-create",
    ),
    path(
        "comments/<int:pk>",
        api_views.CommentDetailAPIView.as_view(),
        name="comments-detail",
    ),
]
