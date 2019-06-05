from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import connections
from django.views.decorators.csrf import csrf_exempt



class login:
    @csrf_exempt
    @api_view(['POST'])
    @permission_classes((AllowAny,))
    def token_login(request):
        # data = request.POST.get('data')
        p_username = request.POST.get("username")
        p_password = request.POST.get("password")
        # return JsonResponse(p_password, safe=False)
        row = dict()
        row['result'] = ''
        row['token'] = ''
        if p_username and p_password:
            refcur = connections['AccountsSys'].cursor()
            refcur.execute("select remember_token from users where username = %s and password = %s and enabled = 1",
                           (p_username, p_password))
            row['token'] = refcur.fetchall()
            if (row['token']):
                row['result'] = "Đăng Nhập Thành Công"
                return Response(row, status=status.HTTP_200_OK)
            else:
                row['result'] = "Sai mật khẩu hoặc tài khoản"
                return Response(row['result'], status=status.HTTP_401_UNAUTHORIZED)
        else:
            row['result'] = "Thiếu mật khẩu hoặc tài khoản"
            return Response(row['result'], status=status.HTTP_400_BAD_REQUEST)
