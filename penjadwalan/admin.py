from django.contrib import admin
from penjadwalan.models import *

# Register your models here.

class MatakuliahAdmin(admin.ModelAdmin):
    list_display = ['matkul', 'sks']
    search_fields = ['matkul', 'sks']
    list_filter = ('sks',)

class RuanganAdmin(admin.ModelAdmin):
    list_display = ['lab', 'keterangan']
    search_fields = ['lab', 'keterangan']

class DosenAdmin(admin.ModelAdmin):
    list_display = ['nama', 'notelp']
    search_fields = ['nama', 'notelp']

class JadwalAdmin(admin.ModelAdmin):
    list_display = ['hari', 'waktu', 'matkul_id', 'lab_id', 'dosen_id']
    list_filter = ('waktu', 'lab_id',)
    list_per_page = 5
    
    

admin.site.register(Ruangan, RuanganAdmin) 
admin.site.register(Matakuliah, MatakuliahAdmin)
admin.site.register(Dosen, DosenAdmin)
admin.site.register(Jadwal, JadwalAdmin)