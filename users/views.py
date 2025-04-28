from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer
from common.utils import standard_response
from common.schemas import StandardResponseSerializer
from drf_spectacular.utils import extend_schema


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class MyView(APIView):
    @extend_schema(responses={200: StandardResponseSerializer})
    def get(self, request):
        data = standard_response(
            success=True,
            message="This is a GET request",
            data={"key": "value"},
            status_code=status.HTTP_200_OK,
        )
        return Response(data, status=status.HTTP_200_OK)
