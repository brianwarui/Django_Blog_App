from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
# Create your models here.

STATUS = (
	(0, 'Publish'),
	(1, 'Draft')

	)


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = RichTextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=STATUS, default=1)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	


	def __str__(self):
		return self.title  




	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})