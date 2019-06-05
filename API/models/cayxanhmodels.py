from django.db import models


class Cayxanh(models.Model):
    objectid = models.IntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    sohieu = models.CharField(db_column='SoHieu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    matencx = models.CharField(db_column='MaTenCX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kinhdo = models.DecimalField(db_column='KinhDo', max_digits=31, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    vido = models.DecimalField(db_column='ViDo', max_digits=31, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    duongkinh = models.DecimalField(db_column='DuongKinh', max_digits=31, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    chieucao = models.DecimalField(db_column='ChieuCao', max_digits=31, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dorongtan = models.DecimalField(db_column='DoRongTan', max_digits=31, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ngaytrong = models.DateTimeField(db_column='NgayTrong', blank=True, null=True)  # Field name made lowercase.
    ngaycapnhat = models.DateTimeField(db_column='NgayCapNhat', blank=True, null=True)  # Field name made lowercase.
    thuoctinh = models.CharField(db_column='ThuocTinh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    matinhtrang = models.IntegerField(db_column='MaTinhTrang', blank=True, null=True)  # Field name made lowercase.
    tuyenduong = models.CharField(db_column='TuyenDuong', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shape = models.TextField(db_column='Shape', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nvks_x = models.DecimalField(db_column='NVKS_X', max_digits=38, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    nvks_y = models.DecimalField(db_column='NVKS_Y', max_digits=38, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    nguoicapnhat = models.CharField(db_column='NguoiCapNhat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    xoabo = models.CharField(db_column='Xoabo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAYXANH'
    def __str__(self):
        return self.sohieu, self.matencx

    def ___init__(self, sohieu):
        self.sohieu = sohieu
