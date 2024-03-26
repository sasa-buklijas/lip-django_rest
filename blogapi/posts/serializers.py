from rest_framework import serializers 
from .models import Post

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        fields = (
            "id",
            "author", 
            "title", 
            "body", 
            "created_at",
        )
        # for what model (Post) is this serializers
        model = Post
