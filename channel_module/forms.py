from django import forms

from account_module.models import User
from post_module.models import Playlist


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'profile_picture', 'channel_banner', 'about_user']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'channel_banner': forms.FileInput(attrs={'placeholder': 'channel banner'}),
            'profile_picture': forms.FileInput(attrs={'placeholder': 'profile picture'}),
            'about_user': forms.Textarea(attrs={'rows': '6'}),
        }


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'is_active', 'thumbnail_url', 'video']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter playlist title'
            }),
            'thumbnail_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional thumbnail URL'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'video': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input'
            }),
        }