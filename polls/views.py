from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.auth import logout

from polls.models import Video

# from django.http import HttpResponse

from polls.forms import VideoForm
from seting.models import Person

# Create your views here.
# from django.http import HttpResponse


# from polls.forms import ShaxsForm
from users.models import MyUseer


def index(request):
    return render(request, "polls.html")


def registration(request):
    if request.method == 'POST':
        new_user = MyUseer.objects.create(
            username=request.POST.get('usrnm'),
        )
        new_user.set_password(request.POST.get('psw'))
        new_user.save()
        return redirect('login')
    return render(request, "registration.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['usrnm']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['usrnm'] = username
            request.session.save()
            return redirect('sahifa')
        else:
            return render(request, 'login.html', {'error_message': 'Natogri login yoki parol'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect('sahifa')


def sahifa(request):
    if request.method == 'POST':
        pass
    return render(request, "bosh_sahifa.html")


def fanlar(request):
    return render(request, "fanlar_t.html")


def upload_form(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'yuklash.html', context)
    context = {'form': VideoForm()}
    return render(request, 'yuklash.html', context)

def video_d(request):
    dogs = Video.objects.all()
    context = {'dogs': dogs}
    return render(request, "video_d.html", context)


def upload_file(request):
    persons = Person.objects.all()
    return render(request, 'yuklash.html', {'persons': persons})


