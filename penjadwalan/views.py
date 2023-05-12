from django.shortcuts import render, redirect
#from django.http import HttpResponse
from penjadwalan.models import *
from penjadwalan.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
import datetime


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan saat membuat akun!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form,
        }
        return render(request, 'signup.html', konteks)


#                                   J A D W A L

def jadwal(request):
    if request.POST:
        keyword = request.POST['cari']
        keyword = keyword.title()
        jdwl = Jadwal.objects.filter(hari__contains=keyword)
        konteks = {
            'jdwl' : jdwl,
        }
    else:
        jdwl = Jadwal.objects.all().order_by('-id')
        paginator = Paginator(jdwl, 5)
        page = request.GET.get('page')
        jdwl = paginator.get_page(page)

        konteks = {
            'jdwl' : jdwl,
        }
    return render(request, 'jadwal.html', konteks) #konteks

@login_required(login_url=settings.LOGIN_URL)
def tambah_jadwal(request):
    if request.POST:
        form = FormJadwal(request.POST)
        if form.is_valid():
            is_bentrok = cek_bentrok(form)
            if is_bentrok:
                messages.error(request, "Jadwal bentrok!")
                return redirect('jadwal')
            form.save()
            form = FormJadwal()
            messages.success(request, "Jadwal berhasil ditambahkan!")
            return redirect('jadwal')
    else:
        form = FormJadwal()
        konteks = {
            'form' : form,
        }
    return render (request, 'tambah-jadwal.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_jadwal(request, id_jadwal):
    jadwal = Jadwal.objects.get(id=id_jadwal)
    template = 'ubah-jadwal.html'
    if request.POST:
        form = FormJadwal(request.POST, instance=jadwal)
        if form.is_valid():
            form.save()
            messages.success(request, "Jadwal berhasil diperbarui!")
            return redirect('ubah_jadwal', id_jadwal = id_jadwal)
    else:
        form = FormJadwal(instance=jadwal)
        konteks = {
            'form' : form,
            'jadwal' : jadwal,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_jadwal(request, id_jadwal):
    jadwal = Jadwal.objects.filter(id=id_jadwal)
    jadwal.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('jadwal')

def cek_bentrok(form_jadwal:FormJadwal):
    input_hari = form_jadwal.cleaned_data['hari']
    input_waktu = form_jadwal.cleaned_data['waktu']
    input_lab = form_jadwal.cleaned_data['lab_id']
    jadwals = Jadwal.objects.filter(hari=input_hari)
    for jadwal in jadwals:
        matkul = jadwal.matkul_id
        sks = matkul.sks
        jam_awal = jadwal.waktu
        jumlah_menit = sks * 50
        now = datetime.datetime.combine(datetime.datetime.today(), jam_awal)
        new_datetime = now + datetime.timedelta(minutes=jumlah_menit)
        jam_akhir = new_datetime.time()
        
        if input_waktu >= jam_awal and input_waktu <= jam_akhir:
            lab = jadwal.lab_id
            if input_lab.id == lab.id :
                return True
    return False



#                                   D O S E N
def dosen(request):
    if request.POST:
        keyword = request.POST['cari']
        keyword = keyword.title()
        dsn = Dosen.objects.filter(nama__contains=keyword)
        konteks = {
            'dsn' : dsn,
        }
    else:
        dsn = Dosen.objects.all().order_by('-id')
        paginator = Paginator(dsn, 5)
        page = request.GET.get('page')
        dsn = paginator.get_page(page)
        konteks = {
            'dsn' : dsn,
        }
    return render(request, 'dosen.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            return redirect('dosen')
    else:
        form = FormDosen()
        konteks = {
            'form' : form,
        }
    return render (request, 'tambah-dosen.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            form.save()
            messages.success(request, "Data berhasil diperbarui!")
            return redirect('ubah_dosen', id_dosen = id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form' : form,
            'dosen' : dosen,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('dosen')


#                                   M A T K U L
def matakuliah(request):
    if request.POST:
        keyword = request.POST['cari']
        keyword = keyword.title()
        matkul = Matakuliah.objects.filter(matkul__contains=keyword)
        konteks = {
            'matkul' : matkul,
        }
    else:
        matkul = Matakuliah.objects.all().order_by('matkul')
        paginator = Paginator(matkul, 5)
        page = request.GET.get('page')
        matkul = paginator.get_page(page)
        konteks = {
            'matkul' : matkul,
        }
    return render(request, 'matakuliah.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_matakuliah(request):
    if request.POST:
        form = FormMatakuliah(request.POST)
        if form.is_valid():
            form.save()
            form = FormMatakuliah()
            return redirect('matakuliah')
    else:
        form = FormMatakuliah()
        konteks = {
            'form' : form,
        }
    return render (request, 'tambah-matakuliah.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_matakuliah(request, id_matakuliah):
    matakuliah = Matakuliah.objects.get(id=id_matakuliah)
    template = 'ubah-matakuliah.html'
    if request.POST:
        form = FormMatakuliah(request.POST, instance=matakuliah)
        if form.is_valid():
            kodematkul = form.cleaned_data['kodematkul']
            matkul = form.cleaned_data['matkul']
            form.save()
            messages.success(request, "Jadwal berhasil diperbarui!")
            return redirect('ubah_matakuliah', id_matakuliah = id_matakuliah)
    else:
        form = FormMatakuliah(instance=matakuliah)
        konteks = {
            'form' : form,
            'matakuliah' : matakuliah,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_matakuliah(request, id_matakuliah):
    matakuliah = Matakuliah.objects.filter(id=id_matakuliah)

    matakuliah.delete()
    messages.success(request, "Data berhasil dihapus!")

    return redirect('matakuliah')


#                                   R U A N G A N
def ruangan(request):
    if request.POST:
        keyword = request.POST['cari']
        keyword = keyword.upper()
        rngn = Ruangan.objects.filter(lab__contains=keyword)
        konteks = {
            'rngn' : rngn,
        }
    else:
        rngn = Ruangan.objects.all().order_by('lab')
        paginator = Paginator(rngn, 5)
        page = request.GET.get('page')
        rngn = paginator.get_page(page)
        konteks = {
            'rngn' : rngn,
        }
    return render(request, 'ruangan.html', konteks) 

@login_required(login_url=settings.LOGIN_URL)
def tambah_ruangan(request):
    if request.POST:
        form = FormRuangan(request.POST)
        if form.is_valid():
            form.save()
            form = FormRuangan()
            return redirect('ruangan')
    else:
        form = FormRuangan()
        konteks = {
            'form' : form,
        }
    return render (request, 'tambah-ruangan.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_ruangan(request, id_ruangan):
    ruangan = Ruangan.objects.get(id=id_ruangan)
    template = 'ubah-ruangan.html'
    if request.POST:
        form = FormRuangan(request.POST, instance=ruangan)
        if form.is_valid():
            lab = form.cleaned_data['lab']
            form.save()
            messages.success(request, "Ruangan berhasil diperbarui!")
            return redirect('ubah_ruangan', id_ruangan = id_ruangan)
    else:
        form = FormRuangan(instance=ruangan)
        konteks = {
            'form' : form,
            'ruangan' : ruangan,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_ruangan(request, id_ruangan):
    ruangan = Ruangan.objects.filter(id=id_ruangan)

    ruangan.delete()
    messages.success(request, "Data berhasil dihapus!")

    return redirect('ruangan')
