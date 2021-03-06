# Generated by Django 2.1.5 on 2019-05-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cayxanh',
            fields=[
                ('objectid', models.IntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('sohieu', models.CharField(blank=True, db_column='SoHieu', max_length=50, null=True)),
                ('matencx', models.CharField(blank=True, db_column='MaTenCX', max_length=10, null=True)),
                ('kinhdo', models.DecimalField(blank=True, db_column='KinhDo', decimal_places=10, max_digits=31, null=True)),
                ('vido', models.DecimalField(blank=True, db_column='ViDo', decimal_places=10, max_digits=31, null=True)),
                ('duongkinh', models.DecimalField(blank=True, db_column='DuongKinh', decimal_places=10, max_digits=31, null=True)),
                ('chieucao', models.DecimalField(blank=True, db_column='ChieuCao', decimal_places=10, max_digits=31, null=True)),
                ('dorongtan', models.DecimalField(blank=True, db_column='DoRongTan', decimal_places=10, max_digits=31, null=True)),
                ('ngaytrong', models.DateTimeField(blank=True, db_column='NgayTrong', null=True)),
                ('ngaycapnhat', models.DateTimeField(blank=True, db_column='NgayCapNhat', null=True)),
                ('thuoctinh', models.CharField(blank=True, db_column='ThuocTinh', max_length=50, null=True)),
                ('ghichu', models.CharField(blank=True, db_column='GhiChu', max_length=50, null=True)),
                ('matinhtrang', models.IntegerField(blank=True, db_column='MaTinhTrang', null=True)),
                ('tuyenduong', models.CharField(blank=True, db_column='TuyenDuong', max_length=20, null=True)),
                ('shape', models.TextField(blank=True, db_column='Shape', null=True)),
                ('nvks_x', models.DecimalField(blank=True, db_column='NVKS_X', decimal_places=8, max_digits=38, null=True)),
                ('nvks_y', models.DecimalField(blank=True, db_column='NVKS_Y', decimal_places=8, max_digits=38, null=True)),
                ('nguoicapnhat', models.CharField(blank=True, db_column='NguoiCapNhat', max_length=200, null=True)),
                ('xoabo', models.CharField(blank=True, db_column='Xoabo', max_length=1, null=True)),
            ],
            options={
                'db_table': 'CAYXANH',
                'managed': False,
            },
        ),
    ]
