from django.contrib import admin
from PIC.models import Pic, PicGroup

__author__ = 'yh'

class PicAdmin(admin.ModelAdmin):
	date_hierarchy = 'create_time'
	list_display = ('name', 'view_count', 'pic', 'create_time' )
	list_display_links = ('name', )
	readonly_fields= ('create_time',)
	search_fields = ('name', 'pic',)
admin.site.register(Pic,PicAdmin)

class PicGroupAdmin(admin.ModelAdmin):
	date_hierarchy = 'create_time'
	list_display = ('name','desc', 'view_count', 'pics', 'create_time','view_count',)
	list_display_links = ('name', )
	readonly_fields= ('create_time','tags')
	search_fields = ('name', 'desc',)
admin.site.register(PicGroup,PicGroupAdmin)