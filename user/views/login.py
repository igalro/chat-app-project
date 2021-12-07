import json

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseBadRequest, JsonResponse
from user.models.user import User


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        body = json.loads(request.body)

        try:
            email = body['email']
            password = body['password']
            user = User.objects.filter(email=email).first()
            if check_password(password, user.password):
                token = PasswordResetTokenGenerator().make_token(user)
            else:
                msg = "User not registered, please register first."
                return HttpResponseBadRequest(msg)
            return JsonResponse({'token': token})
        except:
            return HttpResponseBadRequest()
