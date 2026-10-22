from rest_framework import serializers
from .models import Booking, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory"]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Title cannot be blank.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            "id", "name", "no_of_guests", "booking_date",
            "notes", "created_by", "created_at",
        ]
        read_only_fields = ["id", "created_by", "created_at"]

    def validate_no_of_guests(self, value):
        if value < 1:
            raise serializers.ValidationError("At least one guest is required.")
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["created_by"] = request.user
        return super().create(validated_data)
