from django.shortcuts import render
from .forms import sypmform

def home(request):
    return render(request, 'home.html')

def sypm_data_form(request):
    if request.method == 'POST':
        filled_form : sypmform(request.POST)
        if filled_form.is_valid():
            note = 'Data %s telah disimpan.' %(filled_form.cleaned_data['namamapemohon'])
            new_form = sypmform()
            return render(request, 'sypm_data_form.html', {'sypmform': new_form, 'note':note})
    else:
        form = sypmform()
        return render(request, 'sypm_data_form.html', {'sypmform': form})


#
# def sypm_data_view(request):
#     if request.method == 'POST':
#         form = SypmData(request.POST)
#         if form.is_valid():
#             form.save()
#             new_form = form.sypm_data_form()
#             return render(request, 'sypm_data_form.html',{'form':new_form})
#             # return HttpResponseRedirect('/Terima kasih/')
#     else:
#         form = SypmData()
#         return render(request, 'sypm_data_form.html', {'form': form})
