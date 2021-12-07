from django.conf import settings

from .request import Request
request = Request(settings.AUTHENTICATION_SERVICE)
