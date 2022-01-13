from django.contrib import admin
from.models import Contact,Category,AddPost,Comment

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject','message']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_of_categories']



@admin.register(AddPost)
class AddPostAdmin(admin.ModelAdmin):
    list_display = ['id','blog_title','categories1','description','image','name','email','datetime']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','name','email','comment','image','message','datetime']