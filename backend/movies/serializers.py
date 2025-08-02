# movies/serializers.py

from rest_framework import serializers

ALLOWED_MOODS = ["Sad", "Angry", "Bored", "Romantic", "Happy", "Anxious"]

        
        
        
        
class MoodInputSerializer(serializers.Serializer):
    mood = serializers.CharField(required=True)

    def validate_mood(self, value):
        if value not in ALLOWED_MOODS:
            raise serializers.ValidationError(
                f"'{value}' is not a valid mood. Allowed moods: {', '.join(ALLOWED_MOODS)}"
            )
        return value
    
class MovieResponseSerializer(serializers.Serializer):
    title = serializers.CharField()
    overview = serializers.CharField()
    poster = serializers.URLField()
    mood = serializers.CharField()
