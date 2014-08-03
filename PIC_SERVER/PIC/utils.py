# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import mechanize
import cookielib


def getHtml(url):
	"""
	获取网页内容
	"""
	# page = urllib.urlopen(url)
	html = urllib2.urlopen(url).read()
	# html = page.read()
	return html

def getImg(html):
	"""
	获取图片地址
	"""
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl, '%s.jpg' % x)
		x = x + 1
	return imglist


def getImg2(html):
	reg = r'<img src="(.*?\.\w{3,4})"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	return imglist


def br_get_html(url):
	br = get_br()
	r = br.open(url)
	html = r.read
	return html

def get_br():
	# Browser
	br = mechanize.Browser()
	# Cookie Jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	# Follows refresh 0 but not hangs on refresh > 0
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	return br
