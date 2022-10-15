from django.contrib import admin
from .models import surat_masuk, surat_keluar


admin.site.site_header = 'E-Arsip'
admin.site.index_title = 'E-Arsip'
admin.site.site_title = 'Admin'
# Register your models here.
admin.site.register(surat_masuk)
admin.site.register(surat_keluar)
