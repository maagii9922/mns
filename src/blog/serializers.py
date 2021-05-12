from rest_framework import serializers
from src.blog.models import Blog
from django.conf import settings


SEARCH_PATTERN = 'src="/media/uploads/'
REPLACE_WITH = 'src="{scheme}{domain}/media/uploads/'.format(
    scheme="https://", domain=settings.SITE_DOMAIN
)


class FixAbsolutePathSerializer(serializers.Field):
    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text


class BlogSerializer(serializers.ModelSerializer):
    content = FixAbsolutePathSerializer()

    class Meta:
        depth = 5
        model = Blog
        fields = [
            "id",
            "title",
            "title_en",
            "description",
            "description_en",
            "content",
            "content_en",
            "author",
            "category",
            "tags",
            "publicDate",
            "thumbImage",
            "coverImage",
            "slug",
        ]
        slug = serializers.SlugRelatedField(
            many=True, read_only=True, slug_field="name"
        )
