from django import forms

from account_module.models import User
from post_module.models import Playlist, Post


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'profile_picture', 'channel_banner', 'about_user']
        labels = {
            'username': '',
            'profile_picture': '',
            'channel_banner': '',
            'about_user': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'channel_banner': forms.FileInput(attrs={'placeholder': 'channel banner'}),
            'profile_picture': forms.FileInput(attrs={'placeholder': 'profile picture'}),
            'about_user': forms.Textarea(attrs={'rows': '6'}),
        }


class PlaylistCreationForm(forms.ModelForm):
    video = forms.ModelMultipleChoiceField(
        queryset=Post.objects.none(),
        widget=forms.SelectMultiple(),
        required=False,
        label=''
    )

    class Meta:
        model = Playlist
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        instance = kwargs.get('instance')
        super(PlaylistCreationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['video'].queryset = Post.objects.filter(channel=user, is_active=True)

        if instance:
            self.fields['video'].initial = instance.video.all()


