# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from PIC_SERVER.pic.utils import getImg, getHtml, getImg2, br_get_html


def network_pic(request):
	i = 1000
	img_list = []
	while True:
		website = "http://jandan.net/ooxx/page-%i" % i
		html = getHtml(website)
		i += 1
	# getImg(html)
	# html = br_get_html(website)
		list = getImg2(html)
		if i>1010:
			break
		img_list.extend(list)

	return render_to_response('pic/pic_list.html', locals(), context_instance=RequestContext(request))

def test():
	pass

