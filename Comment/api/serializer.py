from Comment.models import Books, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField(
        read_only=True
    )  # will replace id with name (models Commenter)

    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ["book"]


class BooksSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    # comments = serializers.HyperlinkedRelatedField(
    #     view_name="comments-detail",  # you have to write the name you gave to the view name of url
    #     read_only=True,
    #     many=True,
    # )

    class Meta:
        model = Books
        fields = "__all__"
