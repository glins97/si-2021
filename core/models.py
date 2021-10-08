from django.db import models
from django.contrib.auth.models import User


class Attachment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/attachments/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    body = models.CharField(max_length=100)

    comments = models.ManyToManyField('Comment', related_name='comment_comments')
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes')
    attachments = models.ManyToManyField(Attachment)
    bookmarks = models.ManyToManyField(Bookmark)
    tags = models.ManyToManyField(Tag)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    publication_types = (
        ('hint', 'Dica'),
        ('discussion', 'Discussão'),
        ('notícia', 'Notícia'),
        ('question', 'Pergunta'),
        ('other', 'Outros'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.CharField(max_length=255, choices=publication_types)
    
    comments = models.ManyToManyField(Comment, related_name='publication_comments')
    upvotes = models.ManyToManyField(User, related_name='publication_upvotes')
    attachments = models.ManyToManyField(Attachment)
    bookmarks = models.ManyToManyField(Bookmark)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=8)


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=8)


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=8)


class Neighborhood(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Place(models.Model):
    place_types = (
        ('commerce', 'Comércio'),
        ('leisure', 'Lazer'),
        ('other', 'Outros'),
    )

    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=place_types)
    cover = models.ImageField(upload_to='uploads/places/')

    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True) 
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    comments = models.ManyToManyField(Comment, related_name='places_comments')
    upvotes = models.ManyToManyField(User, related_name='places_upvotes')
    attachments = models.ManyToManyField(Attachment)
    bookmarks = models.ManyToManyField(Bookmark)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name


class AchievementType(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=8)
    description = models.TextField()
    conditions = models.JSONField()


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(AchievementType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/profile/avatars/')
    cover = models.ImageField(upload_to='uploads/profile/covers/')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)
    
