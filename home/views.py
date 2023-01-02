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
    
#trong trường hợp không cần xác thực
from rest_framework import permissions
class NotAuthen(APIView):
    # thêm dòng lệnh này là không cần xác thực
    permission_classes=(permissions.AllowAny,) # chú ý chỗ này có dấu , để mt hiểu đây là tuple chứ không phải string 
    def get(self,request):
        return Response('ok khong can xac thuc')