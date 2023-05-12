from django.forms import ModelForm
from penjadwalan.models import *
from django import forms
from django.forms.widgets import DateInput, TimeInput, Select
from django.utils import formats

class FormJadwal(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'

        labels = {
        'hari': 'Pilih Hari',
        'matakuliah_id': 'Matakuliah',
        'matkul': 'Jumlah SKS',
        'matakuliah_id': 'Matakuliah',
        'dosen_id': 'Dosen',
        'lab_id': 'LAB',
        }   

        HARI_CHOICES= [
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
        ]

        widgets = {
            'hari' : forms.Select(choices=HARI_CHOICES, attrs={'class': 'form-control', 'placeholder': 'Pilih Hari'}),
            'waktu' : forms.TimeInput({'type': 'time', 'attrs': {'class': 'form-control', 'placeholder': 'Masukan Waktu'}}),
            'matakuliah_id' : forms.Select({'class':'form-control', 'attrs': {'placeholder': 'Pilih Matakuliah'}}),
            'dosen_id' : forms.Select({'class':'form-control', 'attrs': {'placeholder': 'Pilih Dosen'}}),
            'lab_id' : forms.Select({'class':'form-control', 'attrs': {'placeholder': 'Pilih Lab'}}),
        }
    def clean_hari(self):
        return self.cleaned_data['hari'].title()

class FormDosen(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'
        labels = {
        'nip': 'NIP',
        'nama': 'Nama',
        'notelp': 'Nomor Telpon',
        'mail': 'E-Mail',
        }   

        widgets = {
            'nip' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan NIP'}),
            'nama' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan Nama'}),
            'notelp' : forms.TextInput({'class':'form-control', 'placeholder': 'Nomor Telpon'}),
            'mail' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan E-mail'}),
        }
    def clean_nama(self):
        return self.cleaned_data['nama'].title()

class FormMatakuliah(forms.ModelForm):
    class Meta:
        model = Matakuliah
        fields = '__all__'

        labels = {
        'kodematkul': 'Kode Matakuliah',
        'matkul': 'Matakuliah',
        'sks': 'Jumlah SKS',
        }   
    
        sks_choice= [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ]

        widgets = {
            'kodematkul' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan Kode Matakuliah'}),
            'matkul' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan Matakuliah'}),
            'sks': forms.Select(choices=sks_choice, attrs={'class': 'form-control', 'placeholder': 'Jumlah SKS'}),
        }
    def clean_kodematkul(self):
        return self.cleaned_data['kodematkul'].upper()
    def clean_matkul(self):
        return self.cleaned_data['kodematkul'].upper()
        

class FormRuangan(forms.ModelForm):
    class Meta:
        model = Ruangan
        fields = '__all__'

        labels = {
        'lab': 'Nama Lab',
        'keterangan': 'Keterangan',
        }   

        widgets = {
            'lab' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan Lab'}),
            'keterangan' : forms.TextInput({'class':'form-control', 'placeholder': 'Masukan Keterangan'}),
        }
    def clean_lab(self):
        return self.cleaned_data['lab'].upper()