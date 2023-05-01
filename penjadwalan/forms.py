from django.forms import ModelForm
from penjadwalan.models import *
from django import forms
from django.forms.widgets import DateInput, TimeInput, Select
from django.utils import formats

class FormJadwal(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'
        HARI_CHOICES= [
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
        ]

        widgets = {
            'hari' : forms.Select(choices=HARI_CHOICES),
            #'tanggal' : forms.DateInput({'type': 'date'}),
            'waktu' : forms.TimeInput({'type': 'time'}),
            'matakuliah_id' : forms.Select({'class':'form-control'}),
            'dosen_id' : forms.Select({'class':'form-control'}),
            'lab_id' : forms.Select({'class':'form-control'}),
        }

class FormDosen(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'notelp' : forms.TextInput({'class':'form-control'}),
            'mail' : forms.TextInput({'class':'form-control'}),
        }

class FormMatakuliah(forms.ModelForm):
    class Meta:
        model = Matakuliah
        fields = '__all__'

        widgets = {
            'kodematkul' : forms.TextInput({'class':'form-control'}),
            'matkul' : forms.TextInput({'class':'form-control'}),
            'sks' : forms.TextInput({'class':'form-control'}),
        }

class FormRuangan(forms.ModelForm):
    class Meta:
        model = Ruangan
        fields = '__all__'

        widgets = {
            'lab' : forms.TextInput({'class':'form-control'}),
            'keterangan' : forms.TextInput({'class':'form-control'}),
        }