from rest_framework.serializers import ModelSerializer
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

    class Meta:
        model = Comment
        fields = '__all__'


class PublicationSerializer(ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'


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

    class Meta:
        model = User
        fields = '__all__'
