from django import forms


# from .models import SypmData
#
#
# class SypmForm(forms.ModelForm):
#     class Meta:
#         model = SypmData
#         fields = ['namapemohon', 'nokp', 'notel', 'alamatsemasa', 'alamat2', 'tahunmula', 'tahunberakhir', 'namabapa',
#                   'notelbapa', 'namaibu', 'notelibu']
#         labels = {'namapemohon': ' Nama Pemohon', 'nokp': 'No KP', 'notel': 'No HP', 'alamatsemasa': 'Alamat Semasa',
#                   'alamat2': 'Alamat Kediaman', 'tahunmula': 'Tahun Bermula', 'tahunberakhir': 'Tahun Berakhir',
#                   'namabapa': 'Nama Bapa', 'notelbapa': 'No Tel Bapa', 'namaibu': 'Nama Ibu', 'notelibu': 'No Tel Ibu'}
class sypmform(forms.Form):
    namapemohon = forms.CharField(label='Nama Pemohon',max_length=100)
    nokp = forms.CharField(label='No KP',max_length=100)
    notel = forms.CharField(label='No HP',max_length=100)
    alamatsemasa = forms.CharField(label='Alamat Semasa',max_length=100)
    alamat2 = forms.CharField(label='Alamat Kediaman',max_length=100)
    tahunmula = forms.CharField(label='Tahun Bermula',max_length=100)
    tahunberakhir = forms.CharField(label='Tahun Berakhir',max_length=100)
    namabapa = forms.CharField(label='Nama Bapa',max_length=100)
    notelbapa = forms.CharField(label='No Tel Bapa',max_length=100)
    namaibu = forms.CharField(label='Nama Ibu',max_length=100)
    notelibu = forms.CharField(label='No Tel Ibu',max_length=100)
    jenisbantuan = forms.ChoiceField(label='Jenis Bantuan',
                                     choices=[('Tunai', 'Tunai'), ('Peralatan Sekolah', 'Peralatan Sekolah'),
                                              ('Keperluan ICT', 'Keperluan ICT')])
