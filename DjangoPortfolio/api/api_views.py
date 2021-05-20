from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

from .models import Project, Image, Tag, DetailBody
from .serializers import ProjectSerializer, ImageSerializer, TagSerializer, DetailBodySerializer

class StandardPagination(LimitOffsetPagination):
    default_limit = 5

class LargerPagination(LimitOffsetPagination):
    default_limit = 10


# API List Views
class ProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    filter_fields = ['tags__name', ] #equality based filter
    search_fields = ['title', 'description', 'tags__name'] #substring based filtering
    pagination_class = StandardPagination

class ImageList(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = LargerPagination

class TagList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    filter_fields = ['name', 'type'] #equality based filter
    search_fields = ['name'] #substring based filtering
    pagination_class = StandardPagination

class DetailBodyList(ListAPIView):
    queryset = DetailBody.objects.all()
    serializer_class = DetailBodySerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['intro', 'body', 'project__id', 'project__title', 'project__description'] #substring based filtering
    pagination_class = StandardPagination


# API Create Views
class ProjectCreate(CreateAPIView):
    serializer_class = ProjectSerializer

class ImageCreate(CreateAPIView):
    serializer_class = ImageSerializer

class TagCreate(CreateAPIView):
    serializer_class = TagSerializer

class DetailBodyCreate(CreateAPIView):
    serializer_class = DetailBodySerializer


# Retrieve Update Destroy Views
class ProjectRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        project_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('project_data_{}', format(id))
        return response

    # need to override update method in order to not have to put in new image every time
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            project = response.data
            cache.set('project_data_{}'.format(id), {
                'title': project['title'],
                'description': project['description'],
                'posted': project['posted'],
                'tags': project['tags'],
                'thumbnail': project['thumbnail'],
                })
        return response

class ImageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        image_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('image_data_{}', format(id))
        return response

    # need to override update method in order to not have to put in new image every time
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            image = response.data
            cache.set('image_data_{}'.format(id), {
                'image': image['image'],
                'project': image['project'],
                })
        return response

class TagRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        tag_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('tag_data_{}', format(id))
        return response

    # need to override update method in order to not have to put in new image every time
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            tag = response.data
            cache.set('tag_data_{}'.format(id), {
                'name': tag['name'],
                'type': tag['type'],
                })
        return response

class DetailBodyRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = DetailBody.objects.all()
    serializer_class = DetailBodySerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        detailbody_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('detailbody_data_{}', format(id))
        return response

    # need to override update method in order to not have to put in new image every time
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            detailbody = response.data
            cache.set('detailbody_data_{}'.format(id), {
                'intro': detailbody['intro'],
                'body': detailbody['body'],
                'project': detailbody['project'],
                })
        return response

