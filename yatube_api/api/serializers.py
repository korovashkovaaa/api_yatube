from rest_framework import serializers
from posts.models import Post, Group, Comment

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created', 'post')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
