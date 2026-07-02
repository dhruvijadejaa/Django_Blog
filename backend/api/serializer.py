from rest_framework import serializers
from .models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    """ This makes Django return full URL instead of just file path """
    featured_image = serializers.SerializerMethodField()

    def get_featured_image(self, obj):

        request = self.context.get('request')

        if obj.featured_image:

            return request.build_absolute_uri(obj.featured_image.url)

        return None

    class Meta:
        model = Blog
        fields = '__all__'  