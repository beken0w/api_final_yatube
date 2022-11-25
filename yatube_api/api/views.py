from posts.models import Post, Follow, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (PostSerializer,
                             CommentSerializer,
                             FollowSerializer,
                             GroupSerializer)
from rest_framework import mixins


class FollowCreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Описание работы представления GroupViewSet.
    GET - api/v1/groups/ - вернет список групп,
    GET - api/v1/groups/{group_id}/- вернет информацию о сообществе по group_id
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    """Описание работы представления PostViewSet.
    GET - api/v1/posts/ - вернет список постов,
    GET - api/v1/posts/{post_id}/ - вернет информацию о посте по post_id,
    POST - api/v1/posts/ - создаст пост на основе переданной информации,
    PUT - api/v1/posts/{post_id}/ - заменит пост с указанным post_id,
    PATCH - api/v1/posts/{post_id}/ - обновит информацию поста по post_id,
    DELETE - api/v1/posts/{post_id}/ - удалит пост по post_id
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Описание работы представления CommentViewSet.
    GET - api/v1/posts/{post_id}/comments - вернет список комментов поста,
    GET - api/v1/posts/{post_id}/comments/{comment_id}/ - вернет коммент,
    POST - api/v1/posts/{post_id}/comments - создаст комментарий для поста,
    PUT - api/v1/posts/{post_id}/comments/{comment_id}/ - заменит коммент,
    PATCH - api/v1/posts/{post_id}/comments/{comment_id}/ - обновит коммент,
    DELETE - api/v1/posts/{post_id}/comments/{comment_id}/ - удалит коммент
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(FollowCreateListViewSet):
    """Описание работы представления FollowViewSet.
    GET - api/v1/follow/ - вернет список подписок,
    POST - api/v1/follow/ - подпишет текущего пользователя на автора
    """
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        following = Follow.objects.filter(user__username=self.request.user)
        return following

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
