#/views.py fayl
from django.shortcuts import render, redirect
from seting.models import Person


#from .forms import KitobForm
#from django.http import FileResponse
#from .models import Kitob

def test(request):
    if request.method == 'POST':
        form = Person.objects.create(
            familya=request.POST.get('f_name'),
            ism=request.POST.get('l_name')
        )
        form.save()
        return redirect('test',)
    return render(request, "test.html")








