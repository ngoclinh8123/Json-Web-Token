from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InforSerializer

# Create your views here.
class TestApiView(APIView):
    def get(self,request):
        return Response('ok')
    def post(self,request):
        da=InforSerializer(data=request.data)
        if not da.is_valid():
            return Response('du lieu khong hop le',status=status.HTTP_400_BAD_REQUEST)
        print(da.data)
        return Response('nhan data thanh cong',status=status.HTTP_200_OK)