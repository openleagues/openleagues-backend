from rest_framework import serializers
from openleagues.authentication.models import User

class UserMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]
