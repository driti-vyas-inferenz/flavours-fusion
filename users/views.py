from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer
from .models import User


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    'message': 'User Created Successfully!',
                    'status': status.HTTP_200_OK,
                    'data': serializer.data
                }
            )
        except ValidationError as ve:
            msg = ve.args[0]
            return Response(
                {
                    'message': msg,
                    'status': status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as ie:
            print("\n Exception --> ", ie)
            return Response(
                {
                    'message': 'Something went wrong. Plz try after sometime.',
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        photo = user.photo.url if user.photo else None,
        return Response(
        {
            'message': 'User Logged In Successfully',
            'status': status.HTTP_200_OK,
            'data': {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'display_name': user.display_name,
                'email': user.email,
                'photo': photo[0],
                'token': token.key,

            }
        }
        )


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({
            'message': 'User Logged Out Successfully!!',
            'status': status.HTTP_200_OK,
        }, status=status.HTTP_200_OK
        )
