from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from core.models import Attachment, Tag, Bookmark, Comment, Publication, Country, State, City, Neighborhood, Place, AchievementType, Achievement, Profile
from core.serializers import AttachmentSerializer, TagSerializer, BookmarkSerializer, CommentSerializer, PublicationSerializer, CountrySerializer, StateSerializer, CitySerializer, NeighborhoodSerializer, PlaceSerializer, AchievementTypeSerializer, AchievementSerializer, ProfileSerializer, UserSerializer


@api_view(['GET', 'POST'])
def attachment_list(request):
    if request.method == 'GET':
        items = Attachment.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = AttachmentSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def attachment_detail(request, pk):
    try:
        item = Attachment.objects.get(pk=pk)
    except Attachment.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AttachmentSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AttachmentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        items = Tag.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = TagSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
    try:
        item = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = TagSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def bookmark_list(request):
    if request.method == 'GET':
        items = Bookmark.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = BookmarkSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def bookmark_detail(request, pk):
    try:
        item = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BookmarkSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookmarkSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        items = Comment.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = CommentSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    try:
        item = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CommentSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def publication_list(request):
    if request.method == 'GET':
        items = Publication.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = PublicationSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def publication_detail(request, pk):
    try:
        item = Publication.objects.get(pk=pk)
    except Publication.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PublicationSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PublicationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        items = Country.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = CountrySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, pk):
    try:
        item = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CountrySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def state_list(request):
    if request.method == 'GET':
        items = State.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = StateSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def state_detail(request, pk):
    try:
        item = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StateSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StateSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        items = City.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = CitySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    try:
        item = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CitySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def neighborhood_list(request):
    if request.method == 'GET':
        items = Neighborhood.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = NeighborhoodSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NeighborhoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def neighborhood_detail(request, pk):
    try:
        item = Neighborhood.objects.get(pk=pk)
    except Neighborhood.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = NeighborhoodSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NeighborhoodSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def place_list(request):
    if request.method == 'GET':
        items = Place.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = PlaceSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def place_detail(request, pk):
    try:
        item = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PlaceSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def achievementtype_list(request):
    if request.method == 'GET':
        items = AchievementType.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = AchievementTypeSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AchievementTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def achievementtype_detail(request, pk):
    try:
        item = AchievementType.objects.get(pk=pk)
    except AchievementType.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AchievementTypeSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AchievementTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def achievement_list(request):
    if request.method == 'GET':
        items = Achievement.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = AchievementSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AchievementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def achievement_detail(request, pk):
    try:
        item = Achievement.objects.get(pk=pk)
    except Achievement.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AchievementSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AchievementSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        items = Profile.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = ProfileSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    try:
        item = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        items = User.objects.order_by('pk').filter(**{key: request.data[key] for key in request.data})
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        item = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
