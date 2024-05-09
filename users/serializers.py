from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    gender =serializers.ChoiceField(User.GENDER, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'first_name', 'last_name', 'gender', 'photo', 'display_name', 'mobile')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'gender': {'required': True},
            'mobile': {'required': True},
            'display_name': {'required': True},
            'photo':  {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        photo = validated_data['photo'] if 'photo' in validated_data.keys() else None
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile=validated_data['mobile'],
            display_name=validated_data['display_name'],
            gender=validated_data['gender'],
            photo=photo
        )

        user.set_password(validated_data['password'])
        user.save()

        return user