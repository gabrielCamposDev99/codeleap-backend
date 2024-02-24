from rest_framework import serializers
from post_api.models import PostModel


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'