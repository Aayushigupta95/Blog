from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    name = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=50, null=True)
    subject = models.CharField(max_length=40, null=True)
    message = models.TextField(max_length=40, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name_of_categories = models.CharField(max_length=200,null=True)
    

    def __str__(self):
        return self.name_of_categories

class AddPost(models.Model):
    blog_title = models.CharField(max_length=50,null=True)
    categories1 = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    description = RichTextField()
    image = models.ImageField(upload_to ='uploads/')
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id

class Comment(models.Model):
    CHOICES =(
            ('good', 'good'),
            ('verygood', 'verygood'),
            ('best', 'best'),
            ('excellent', 'excellent'),
        )
    
    blog = models.ForeignKey(AddPost,on_delete=models.CASCADE,null=True)
    comment = models.CharField(max_length=300, choices = CHOICES,null=True)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    message = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to ='media/')
    datetime = models.DateTimeField(auto_now_add=True)
    def __int__(self):
        return self.blog.id

# {{categories__name_of_categories}}


