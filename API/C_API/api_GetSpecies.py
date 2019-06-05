from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


class TenCayXanh:

    @csrf_exempt
    def getTenCX(request):
        refcur = connections['DoThi'].cursor()
        refcur.execute("select MaTenCX, TenCX from sde.TenCX ")
        row = dict()
        row = refcur.fetchall()
        return JsonResponse(row, safe=False)

    #     Xem Chi Tiết
    @csrf_exempt
    def detailSpecies(request):
        maten = request.POST.get("MaTenCX")
        det = connections['DoThi'].cursor()
        row = dict()
        det.execute("Select * from sde.TenCX where MaTenCX = %s", [maten])
        row['chitiet'] = det.fetchall()
        return JsonResponse(row, safe=False)
