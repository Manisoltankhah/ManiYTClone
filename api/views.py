from django.contrib.auth import authenticate, login

from post_module.models import Post, PostComments, Playlist, PlaylistVideo
from account_module.models import User
from .serializer import UserSerializer, PostSerializer, PostCommentSerializer, PlaylistSerializer, PlaylistVideosSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination


class ResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# User apis
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = ResultSetPagination

    def delete(self, request, *args, **kwargs):
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserRegisterAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "You logged in successfully."}, status=status.HTTP_200_OK)
            return Response({"error":"Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# all post apis
class PostListAPIView(APIView):
    pagination_class = ResultSetPagination
    def get(self, request, format=None):
        title = request.query_params.get("title","")

        if title:
            posts = Post.objects.filter(title= title)
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        Post.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(channel=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(channel=self.request.user)
        else:
            print(serializer.errors)


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(channel=user)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class PostCommentAPIView(APIView):
    pagination_class = ResultSetPagination
    def get(self, request, format=None):
        text = request.query_params.get("text", "")
        if text:
            post_comments = PostComments.objects.filter(text=text)
        else:
            post_comments = PostComments.objects.all()
        serializer = PostCommentSerializer(post_comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        PostComments.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCommentListCreate(generics.ListCreateAPIView):
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PostComments.objects.filter(channel=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user_id=self.request.user.id)


class PostCommentDelete(generics.DestroyAPIView):
    queryset = PostComments.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PostComments.objects.filter(user_id=user.id)


class PostCommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComments.objects.all()
    serializer_class = PostCommentSerializer
    lookup_field = 'pk'


class PlaylistAPIView(APIView):
    pagination_class = ResultSetPagination
    def get(self, request, format=None):
        title = request.query_params.get("title", "")
        if title:
            playlist = Playlist.objects.filter(title= title)
        else:
            playlist = Playlist.objects.all()
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        Playlist.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaylistListCreate(generics.ListCreateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResultSetPagination

    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(user=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)


class PlaylistDelete(generics.DestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(user=user)


class PlaylistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_field = 'pk'


class PlaylistVideoAPIView(APIView):
    def get(self, request, format=None):
        id = request.query_params.get("id", "")
        if id:
            playlist_video = PlaylistVideo.objects.filter(id=id)
        else:
            playlist_video = PlaylistVideo.objects.all()
        serializer = PlaylistVideosSerializer(playlist_video, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        PlaylistVideo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaylistVideoListCreate(generics.ListCreateAPIView):
    serializer_class = PlaylistVideosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PlaylistVideo.objects.filter(channel=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)


class PlaylistVideoDelete(generics.DestroyAPIView):
    queryset = PlaylistVideo.objects.all()
    serializer_class = PlaylistVideosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PostComments.objects.filter(user=user)


class PlaylistVideoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistVideo.objects.all()
    serializer_class = PlaylistVideosSerializer
    lookup_field = 'pk'

