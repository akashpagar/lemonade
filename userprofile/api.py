from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import ForcedResponse
from userprofile.utils import get_user_details


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    setattr(request, 'user', user)
    print(request.user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def logoutsession(request):
    try:
        user_token = Token.objects.get(user=request.user)
        user_token.delete()
    except (Token.DoesNotExist, ValidationError):
        raise ForcedResponse({'detail': 'user not found'})
    return Response({'details': 'user is logout'},
                    status=HTTP_200_OK)


class GetProfile(APIView):
    def get(self, request, *args, **kwargs):
        # TODO: call javascript function which will return profile details
        # TODO: js function will call another python function to get profile details and return in JS

        q = Token.objects.all()
        from django.forms.models import model_to_dict
        data = model_to_dict(q[0])
        print(data)
        from django.conf import settings
        import os

        path_to_js = os.path.join(settings.BASE_DIR, 'userprofile/custom.js')
        with open(path_to_js, 'r') as fd:
            jsdata = fd.read()

        import execjs
        ctx = execjs.compile(jsdata)

        res = ctx.call("helloWorld", 1) # calling helloWorld function of JS
        return Response({'details': 'hello', 'data': res, 'tokens':data})
