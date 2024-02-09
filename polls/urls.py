
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from seting.views import test
from .views import index, registration, login_view, sahifa, fanlar, video_d, upload_form

urlpatterns = [
    path("polls/", index, name="index"),
    path('', registration, name="registration"),
    path("login/", login_view, name="login"),
    path('sahifa/', sahifa, name="sahifa"),
    path('fanlar/', fanlar, name="fanlar"),
    path('test/', test, name="test"),
    path('video_d/', video_d, name="video_d"),
    path('yuklash/', upload_form, name="yuklash"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
