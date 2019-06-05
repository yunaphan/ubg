from django.http import request
from  django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connections

class TuyenDuong:

    def getListRoute(self):
        refcur = connections["DoThi"].cursor()
        refcur.execute("Select MaDuong, TenDuong from sde.TIMDUONG")
        row = dict()
        row = refcur.fetchall()
        return JsonResponse(row, safe=False)
