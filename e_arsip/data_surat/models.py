from tabnanny import verbose
from django.db import models


# Create your models here.


class surat_masuk(models.Model):
    kode_surat = models.CharField(max_length=100)
    tanggal_terima = models.DateField()
    nomor_surat = models.IntegerField()
    pengirim = models.CharField(max_length=100)
    perihal = models.CharField(max_length=100)
    ditunjukan = models.CharField(max_length=100)
    file = models.FileField(
        upload_to='surat_masuk/%Y/%m/%d', help_text='Upload document')

    def __str__(self):
        return "{}.{}".format(self.kode_surat, self.nomor_surat)

    class Meta:
        verbose_name_plural = "Surat Masuk"


class surat_keluar(models.Model):
    kode_surat = models.CharField(max_length=100)
    tanggal_terima = models.DateField()
    nomor_surat = models.IntegerField()
    pengirim = models.CharField(max_length=100)
    perihal = models.CharField(max_length=100)
    ditunjukan = models.CharField(max_length=100)
    file = models.FileField(
        upload_to='surat_keluar/%Y/%m/%d', help_text='Upload document')

    def __str__(self):
        return "{}.{}".format(self.kode_surat, self.nomor_surat)

    class Meta:
        verbose_name_plural = "Surat Keluar"
