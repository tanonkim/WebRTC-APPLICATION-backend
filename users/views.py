from rest_framework                  import status
from rest_framework.views            import APIView
from rest_framework.generics         import CreateAPIView
from rest_framework.response         import Response
from rest_framework.authtoken.models import Token

from users.serializers               import UserSignUpSerializer, UserSignInSerializer

class SignupView(CreateAPIView):
    
    serializer_class = UserSignUpSerializer
    

class SigninView(APIView):
    
    def post(self, request):

        if request.data.get('email') is None or request.data.get('password') is None:
            return Response({'message':['email 또는 password를 입력해주세요.']}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        user = serializer.validated_data['user']

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})