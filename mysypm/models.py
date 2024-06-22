from django.db import models


class SypmData(models.Model):
    # tarikh = models.DateField()
    namapemohon = models.CharField(max_length=255)
    nokp = models.CharField(max_length=255)
    notel = models.CharField(max_length=255)
    # notel2 = models.CharField(max_length=255)
    # jenisbantuan = models.CharField(max_length=255)
    tahunmula = models.CharField(max_length=255)
    tahunberakhir = models.CharField(max_length=255)
    amaunbantuan = models.IntegerField()
    alamatsemasa = models.TextField(max_length=255)
    alamat2 = models.TextField(max_length=255)
    namabapa = models.CharField(max_length=255)
    # nokpbapa = models.CharField(max_length=255)
    notelbapa = models.CharField(max_length=255)
    # pekerjaan = models.CharField(max_length=255)
    namaibu = models.CharField(max_length=255)
    # nokpibu = models.CharField(max_length=255)
    notelibu = models.CharField(max_length=255)
    # kaum = models.CharField(max_length=255)
    # user = models.CharField(max_length=255)

    class Meta:
        db_table = 'sypm_data'

    def __str__(self):
        return self.nokp

    def is_valid(self):
        pass

    def sypm_data_form(self):
        pass

# Create your models here.
