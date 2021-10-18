from django.contrib import admin

from .models import Attachment, Tag, Bookmark, Comment, Publication, Country, State, City, Neighborhood, Place, AchievementType, Achievement, Profile


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'body', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    raw_id_fields = (
        'comments',
        'upvotes',
        'attachments',
        'tags',
    )
    date_hierarchy = 'created_at'


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'body',
        'type',
        'created_at',
        'updated_at',
    )
    list_filter = ('user', 'created_at', 'updated_at')
    raw_id_fields = (
        'comments',
        'upvotes',
        'attachments',
        'tags',
    )
    date_hierarchy = 'created_at'


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abbreviation')
    search_fields = ('name',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'name', 'abbreviation')
    list_filter = ('country',)
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'name', 'abbreviation')
    list_filter = ('state',)
    search_fields = ('name',)


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'name')
    list_filter = ('city',)
    search_fields = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'telephone',
        'instagram',
        'description',
        'type',
        'city',
        'neighborhood',
        'address',
        'created_at',
        'updated_at',
    )
    list_filter = ('city', 'neighborhood', 'created_at', 'updated_at')
    raw_id_fields = (
        'comments',
        'upvotes',
        'attachments',
        'tags',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(AchievementType)
class AchievementTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'abbreviation',
        'description',
        'conditions',
    )
    search_fields = ('name',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'created_at')
    list_filter = ('user', 'type', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'avatar',
        'cover',
        'city',
        'neighborhood',
        'address',
        'phone',
        'email',
        'instagram',
        'facebook',
        'twitter',
        'linkedin',
        'description',
    )
    list_filter = ('user', 'city', 'neighborhood')