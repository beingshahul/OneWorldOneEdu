from django.contrib import admin
from app.models import *


class CourseAdmin(admin.ModelAdmin):
	fieldsets= [ 
		( None , { 'fields' : ['title', 'link',] } ),
		# ( 'Description' , { 'fields' : ['description', 'provider', 'language'] , 'classes' : ['collapse'] }),
		# ( 'Date Information' , { 'fields' : ['pubDate',] , 'classes' : ['collapse'] } ),
		( 'Description' , { 'fields' : ['description', 'provider', 'language',] } ),
		( 'Rating Deatils', { 'fields' : ['rating','panel_rating',] } ),
		( 'Permissions' , { 'fields' : ['category','tags',] } ),
		( 'Date Information' , { 'fields' : ['pubDate',] } ),
	]
	list_filter = ['provider','language']
	list_display = ('title', 'provider', 'language')
	search_fields = ['title']

admin.site.register(OpenCourse,CourseAdmin)
admin.site.register(Category)
admin.site.register(Tags)