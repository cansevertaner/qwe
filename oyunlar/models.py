from django.db import models
import datetime,os
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Count
# Create your models here.
from django.utils.safestring import mark_safe


class Votes(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    value_sts = models.CharField(null=True, max_length=1)
class Comments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    comment_text = models.CharField(max_length=500)
    publish_date = models.DateTimeField(null=False,blank=False,default=datetime.datetime.now())
    def __unicode__(self):
        return str(self.user)
    def __str__(self):
        return str(self.user)
class Votes(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    value_sts=models.CharField(null=True,max_length=1)
class Games(models.Model):
    game_title = models.CharField(max_length=200)
    game_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    game_img = models.FileField(upload_to='oyunlar/static/images/')
    img_name = models.CharField(max_length=200)
    votes = GenericRelation(Votes)
    comments = GenericRelation(Comments)
    def get_vote_count_pos(self):
        counts = Games.objects.filter(id=self.id,votes__value_sts=1).annotate(total_vote=Count('votes'))
        if counts:
            return counts[0].total_vote
        else:
            return 0

    def get_vote_count_neg(self):
        counts = Games.objects.filter(id=self.id,votes__value_sts=2).annotate(total_vote=Count('votes'))
        if counts:
            return counts[0].total_vote
        else:
            return 0

    def get_vote_count(self):
        return self.get_vote_count_pos() - self.get_vote_count_neg()
    def __str__(self):
        return self.game_title