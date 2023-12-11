from rest_framework import serializers
from albums.serializers import AlbumSerializer
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "album_id", "title", "duration"]
        depth = 1
        
    def create(self, validated_data):
        return Song.objects.create(**validated_data)
