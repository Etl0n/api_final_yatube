from rest_framework.exceptions import APIException
from rest_framework import status


class FollowExit(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
