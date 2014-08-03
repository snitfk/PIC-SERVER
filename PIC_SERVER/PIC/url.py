# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
urlpatterns = patterns('PIC_SERVER.pic.views',

	url(r'^$',                                  'network_pic',       name='pic_network_pic'),

)