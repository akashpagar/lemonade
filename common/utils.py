from django.http import JsonResponse
from rest_framework import status


class ForcedResponse(Exception):
    def __init__(self, response, extra_data="", status_code=status.HTTP_200_OK):
        response = response.copy()
        if extra_data or not response.get("extra_data", None):
            response['extra_data'] = extra_data
        self.response = JsonResponse({"status": response, "data": {}})
        self.response.error = True
        self.response.status_code = status_code