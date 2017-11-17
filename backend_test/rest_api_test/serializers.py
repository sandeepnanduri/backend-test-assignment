from rest_api_test.models import Users

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'role')
