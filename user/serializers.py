from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        email = data.get("email","")
        password = data.get("password","")

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    data['token'] = token
                else:
                    raise exceptions.ValidationError("Account is deactivated.")
            else:
                raise exceptions.AuthenticationFailed("Email and password not match.")
        else:
            raise exceptions.ValidationError("Must provide email and password.")

        return data

class RegisterSerializer(serializers.Serializer):
    
    email = serializers.EmailField(max_length=200)
    name = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8)

    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            raise exceptions.ValidationError("Email already exists.")
        else:
            return email            

    def save(self):
        user = User(
            email=self.validated_data['email'],
            name = self.validated_data['name']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user