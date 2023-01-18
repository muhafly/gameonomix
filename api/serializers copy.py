from rest_framework import serializers
from . import Score

class ScoreSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    habit = serializers.IntegerField()
    score = serializers.IntegerField()

    def create(self, validated_data):
        return Score(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
            return instance