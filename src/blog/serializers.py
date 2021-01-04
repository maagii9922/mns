from rest_framework import serializers
from src.blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 5
        model = Blog
        fields = ["id", "title", "description", "content", "author", "category", "tags", "publicDate", "thumbImage", "coverImage", "slug"]
        slug = serializers.SlugRelatedField(
            many=True, read_only=True, slug_field="name"
        )
