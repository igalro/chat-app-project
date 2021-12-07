from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from user.serializers.user import UserSerializer, UserModelSerializer
from user.models.user import User


class UserRegistrationView(ListCreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User(
                username=serializer.data.get('username'),
                password=serializer.data.get('password'),
                email=serializer.data.get('email')
            )
            if user is not None:
                user.set_password(serializer.data.get('password'))
                user.save()
                return JsonResponse(UserModelSerializer(user).data, status=status.HTTP_201_CREATED)
            else:
                user = User.objects.filter(username=serializer.data.get('username')).first()
                user.set_unusable_password()
                user.save()
                return JsonResponse(UserModelSerializer(user).data, status=status.HTTP_201_CREATED)
        return JsonResponse(data={'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        pass
