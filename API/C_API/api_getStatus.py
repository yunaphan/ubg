from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class TrangThai:


    @csrf_exempt
    # lấy danh sách trạng thái cây xanh
    def getListStatusTree(request):
        refcur = connections['DoThi'].cursor()
        refcur.execute("select MaTinhTrang, TinhTrang, GhiChu from sde.TrangThaiCX ")
        row = dict()
        row = refcur.fetchall()
        return JsonResponse(row, safe=False)

    # Xem chi tiết
    @csrf_exempt
    def stastusDetail(request):
        id = request.POST.get('id')
        detail = connections['DoThi'].cursor()
        detail.execute("select * from sde.TrangThaiCX where maTinhTrang = %s", (id))
        detailStatus = dict()
        detailStatus = detail.fetchall()
        return JsonResponse(detailStatus, safe=False)

    @csrf_exempt
    # Thêm Trạng Thái Cây Xanh
    def createStatus(request):
        ma = request.POST.get('matinhtrang')
        ten = request.POST.get('tinhtrang')
        g_chu = request.POST.get('ghichu')
        cre = connections['DoThi'].cursor()
        cre.execute("insert into sde.TrangThaiCX( MaTinhTrang, TinhTrang, GhiChu) values(%s, %s, %s)", (ma, ten, g_chu))
        return JsonResponse({'success': '200'}, safe=False)

    @csrf_exempt
    #     xóa trạng thái
    def deleteStatus(request):
        ma = request.POST.get('matt')
        delete = connections['DoThi'].cursor()
        delete.execute("delete sde.TrangThaiCX where MaTinhTrang = %s (update sde.CAYXANH set MaTinhTrang = 8 where MaTinhTrang = %s) ", (ma))
        return JsonResponse({'success': '200'}, safe=False)


