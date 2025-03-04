from django import forms
from .models import Post, Playlist
from .models import PostComments


class PostCreatingForm(forms.ModelForm):
    playlists = forms.ModelMultipleChoiceField(
        queryset=Playlist.objects.filter(is_active=True),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Add to Playlists'
    )
    class Meta:

        model = Post
        fields = ['video', 'title', 'description', 'thumbnail', 'playlists']
        labels = {
            "video": "",
            "title": "",
            "description": "",
            "thumbnail": "",
        }
        widgets = {
            'video': forms.FileInput({
                "placeholder": "Select a video",

            }),
            'title': forms.TextInput({
                "placeholder": "Add a title for your post",
            }),
            'description': forms.Textarea({
                "placeholder": "Write your post description",
            }),
            'thumbnail': forms.FileInput({
                "placeholder": "Select a thumbnail",
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the view
        super().__init__(*args, **kwargs)
        if user:
            self.fields['playlists'].queryset = Playlist.objects.filter(channel=user, is_active=True)


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ['text']
        labels = {
            "text":""
        }
        widgets = {
            'text': forms.TextInput({
                "placeholder": "Add a Public Comment"
            })
        }


class PostCommentUpdateForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ['text']
        labels = {
            "text": ""
        }
        widgets = {
            'text': forms.TextInput({
                "class": "comment-input"
            })
        }