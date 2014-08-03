# -*- coding: utf-8 -*-
import logging
from django.contrib.auth.models import User
from django.db import models
from stdimage.fields import StdImageField
from taggit.managers import TaggableManager

logger = logging.getLogger(__name__)

class PicGroup(models.Model):
	"""
	图集对象
	"""
	name = models.CharField(max_length=100, null=False, blank=False, verbose_name='图集名称')
	desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='图集介绍')
	poster = models.CharField(max_length=1000, null=True, blank=True, verbose_name='图集海报地址')
	pics = models.TextField(max_length=2000,null=True,blank=True,verbose_name='图集中图片内容')
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
	view_count = models.IntegerField(default=0, null=False, blank=False, verbose_name='图集访问次数')
	create_user = models.OneToOneField(User, null=False, blank=False, verbose_name='创建图集用户')
	tags = TaggableManager(blank=True, verbose_name="标签", help_text="多个标签用comma分隔")

class Pic(models.Model):
	"""
	单个图片对象
	"""
	name = models.CharField(max_length=100, null=False, blank=False, verbose_name='图片名称')
	view_count = models.IntegerField(default=0, null=False, blank=False, verbose_name='图片访问次数')
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
	group = models.ForeignKey(PicGroup,null=True, blank=True, verbose_name='图集名称')
	pic = models.CharField(max_length=1000, null=False, blank=False, verbose_name='图片路径')
	tags = TaggableManager(blank=True, verbose_name="标签", help_text="多个标签用comma分隔")


