from rest_framework   import serializers

from users.models     import User
from users.validators import validate_password


class UserSignUpSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not validate_password(data['password']):
            raise serializers.ValidationError('숫자와 영문자 조합 8자를 입력해주세요')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email      = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name  = validated_data['last_name'],
            password   = validated_data['password']
        )
        user.save()
        return user
    
    class Meta:
        model  = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserSignInSerializer(serializers.Serializer):
        
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)
        
    def validate(self, data):
        email    = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
            
            if not user.check_password(password):
                raise serializers.ValidationError('올바른 password를 입력해주세요')
            
            data['user'] = user
            return data
        
        except User.DoesNotExist:
            raise serializers.ValidationError("사용자가 존재하지 않습니다.")