from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        ref_name = 'CustomUserSerializer'

    def validate(self, data):
        password = data.get('password')
        data['password'] = make_password(password)
        return data
