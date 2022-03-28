from rest_framework.generics import CreateAPIView

from users.serializers       import UserSignUpSerializer


class SignupView(CreateAPIView):
    
    serializer_class = UserSignUpSerializer