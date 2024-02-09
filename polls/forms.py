from django import forms

from polls.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'image')