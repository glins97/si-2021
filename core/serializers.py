from rest_framework.serializers import ModelSerializer, CharField, JSONField, FileField
from django.contrib.auth.models import User
from core.models import Attachment, Tag, Bookmark, Comment, Publication, Country, State, City, Neighborhood, Place, AchievementType, Achievement, Profile


class AttachmentSerializer(ModelSerializer):

    class Meta:
        model = Attachment
        fields = '__all__'


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class BookmarkSerializer(ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    user__avatar = CharField(source='user.profile.avatar', required=False)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user__avatar', 'body', 'comments', 'upvotes', 'attachments', 'tags', 'created_at', 'updated_at']


class PublicationSerializer(ModelSerializer):
    user__first_name = CharField(source='user.first_name', required=False)
    user__last_name = CharField(source='user.last_name', required=False)
    user__username = CharField(source='user.username', required=False)
    user__avatar = CharField(source='user.profile.avatar', required=False)

    class Meta:
        model = Publication
        fields = ['id', 'title', 'body', 'type', 'created_at', 'updated_at', 'user', 'user__first_name', 'user__last_name', 'user__username', 'user__avatar', 'comments', 'upvotes']
        depth = 2

class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class NeighborhoodSerializer(ModelSerializer):

    class Meta:
        model = Neighborhood
        fields = '__all__'


class PlaceSerializer(ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class AchievementTypeSerializer(ModelSerializer):

    class Meta:
        model = AchievementType
        fields = '__all__'


class AchievementSerializer(ModelSerializer):

    class Meta:
        model = Achievement
        fields = '__all__'


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    avatar = FileField(source='profile.avatar')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'avatar']
        depth = 2
