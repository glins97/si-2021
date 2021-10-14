# Generated by Django 3.2.8 on 2021-10-14 00:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='attachments',
            field=models.ManyToManyField(blank=True, null=True, to='core.Attachment'),
        ),
        migrations.AlterField(
            model_name='place',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, null=True, to='core.Bookmark'),
        ),
        migrations.AlterField(
            model_name='place',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='places_comments', to='core.Comment'),
        ),
        migrations.AlterField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='place',
            name='upvotes',
            field=models.ManyToManyField(blank=True, null=True, related_name='places_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
