from rest_framework import serializers
from .models import Movie, ratingMovie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(default=None, required=False)
    rating = serializers.ChoiceField(
        choices=ratingMovie.choices,
        default=ratingMovie.G,
        required=False
    )
    synopsis = serializers.CharField(
        default=None,
        required=False
    )
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
