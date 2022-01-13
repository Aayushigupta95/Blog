from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .import views
  
urlpatterns = [
    path('about', views.About , name='about'),
    path('', views.Index , name='index'),
    path('addblogpost', views.AddBlogPost , name='addblogpost'),
    path('signup', views.Signup , name='signup'),
    path('login', views.Login , name='login'),
    path('logout', views.Logout , name='logout'),
    path('contact', views.ContactUs , name='contact'),
    path('updateblog/<str:pk>', views.UpdateBlog , name='updateblog'),
    path('deleteblog/<str:pk>', views.DeleteBlog , name='deleteblog'),
   
    path('addcomment',views.AddComment, name = 'addcomment'),
    path('blogdetail/<str:pk>/',views.Blogdetail, name = 'blogdetail'),
  

]