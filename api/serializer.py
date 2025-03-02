from rest_framework import serializers
from account_module.models import User
from post_module.models import Post, PostComments, Playlist, PlaylistVideo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'channel_banner', 'slug', 'about_user', 'profile_picture']
        # extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'thumbnail', 'video', 'description', 'slug', 'is_active', 'created_date', 'likes', 'dislike']
        extra_kwargs = {'channel': {'read_only': True}}

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['id', 'post','user','created_date','text']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id','title', 'slug','thumbnail_url', 'video', 'channel', 'is_active']


class PlaylistVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistVideo
        fields = ['id','playlist', 'video']