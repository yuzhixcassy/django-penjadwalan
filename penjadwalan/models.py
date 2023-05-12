from django.db import models

# Create your models here.

class Ruangan(models.Model):
    lab = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.lab

class Matakuliah(models.Model):
    kodematkul = models.CharField(max_length=5, null=True)
    matkul = models.CharField(max_length=50)
    sks = models.IntegerField(null=True) #konversi sks ke menit atau dijadiin menit langsung
    
    def __str__(self):
        return self.matkul

class Dosen(models.Model):
    nip = models.CharField(max_length=10, null=True, blank=True)
    nama = models.CharField(max_length=50)
    notelp = models.CharField(max_length=12, null=True, blank=True)
    mail = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nama

class Jadwal(models.Model):
    hari = models.CharField(max_length=10,null=True)
    #tanggal = models.DateField(null=False)
    waktu = models.TimeField(null=True)
    lab_id = models.ForeignKey(Ruangan, on_delete=models.CASCADE, null=True)
    matkul_id = models.ForeignKey(Matakuliah, on_delete=models.CASCADE, null=True, blank=True)
    dosen_id = models.ForeignKey(Dosen, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.hari
    
class Tempat(models.Model):
    kelompok_kelas = models.CharField(max_length=2, null=True)
    jadwal_id = models.ForeignKey(Jadwal, on_delete=models.CASCADE, null=True, blank=True)
    ruangan_id = models.ForeignKey(Ruangan, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.kelompok_kelas