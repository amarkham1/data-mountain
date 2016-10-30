from __future__ import unicode_literals
from django.utils import timezone
import datetime
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('books.Category', related_name='%(class)s_slug')
	created_date = models.DateTimeField(
            default = timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __unicode__(self):
		return '%s' % self.title
		
	def get_absolute_url(self):
		return "/%s/%s/" % (self.category, self.slug)
		
	def get_absolute_url_bt(self):
	    return "/blogtopics/%s/%s/" % (self.category, self.slug)
		
    
class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	
	def __unicode__(self):
		return '%s' % (self.slug)

