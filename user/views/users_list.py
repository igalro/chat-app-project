from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from user.models.user import User
from django.http import HttpResponseBadRequest, JsonResponse


class GetAllUsersView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):

        try:
            users_list = User.objects.values()
            return JsonResponse(list(users_list), safe=False)
        except:
            return HttpResponseBadRequest()
