from rest_framework import serializers
from .models import Post, PostComments, Playlist, PlaylistVideo

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'thumbnail', 'video', 'description', 'slug', 'is_active', 'created_date', 'channel', 'likes', 'dislike']
#
#     def create(self, validated_data):
#         post = Post.objects.create(**validated_data)
#         return post
#
# class PostCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostComments
#         fields = ['id', 'post','user','created_date','text']
#
# class PlaylistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Playlist
#         fields = ['id','title', 'slug','thumbnail_url', 'video', 'channel', 'is_active']
#
# class PlaylistVideosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlaylistVideo
#         fields = ['id','playlist', 'video']