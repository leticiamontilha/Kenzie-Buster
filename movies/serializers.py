from rest_framework import serializers
from .models import Movie, ratingMovie, MovieOrder


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


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        source="movie.title",
        read_only=True
    )
    price = serializers.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    buyed_by = serializers.SerializerMethodField(
        source="user.email",
        read_only=True
    )
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_buyed_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)