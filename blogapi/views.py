from django.shortcuts import render
from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm
from .form import UserForm  
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate ,logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from.models import Contact,Category,AddPost,Comment
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# from rest_framework.decorators import api_view


def About(request):
    return render(request, "about.html")


def Index(request):
	allblog = AddPost.objects.all()
	if "q" in request.GET:
		q = request.GET["q"] ### single_select
		allblog = AddPost.objects.filter(blog_title__icontains=q)
		paginator = Paginator(allblog, per_page=3)
		page_number = Paginator.Get.get('page',1)
		page_obj = paginator.get_page(page_number)
		return render(request, 'index.html',{'paginator':paginator,'page_number':int(page_number)})
	
	return render(request, 'index.html',{'allblog':allblog})





def Blogdetail(request,pk):
	
	blogdetail=AddPost.objects.get(id=pk)
	
	comment1 = Comment.objects.filter(blog_id = blogdetail.id)
	count = comment1.count()
	print(count)
	if request.method == "POST" and request.FILES['image']:
	
		blog = request.POST.get('blog')
		comment = request.POST.get('Comment')
		image = request.FILES['image']
		name = request.POST.get('name')
		message = request.POST.get('message')
		email = request.POST.get('email')
		blog = blogdetail.id
		print(blog)
		if Comment.objects.filter(blog_id=blogdetail.id,email=email):
			messages.warning(request,"user already comment on this post")
			return redirect("index")
		else:

			comment = Comment(blog_id=blogdetail.id,comment=comment,image=image,name=name,message=message,email=email)
			comment.save()
			return render(request, 'blogdetail.html')
	
		
	
	
		
	return render(request, 'blogdetail.html',{'blogdetail':blogdetail,'comment1':comment1,'count':count})
	
    




def Signup(request):
    if request.method == "POST":  
		# email = request.POST.get('email')
        form = UserForm(request.POST)  
        if form.is_valid():  
            form.save()
			# response = send_email(
            #             subject = 'Blog Message',
            #             message = 'yor registered successfully',
            #             from_email = 'webnetbelgium@gmail.com',
            #             recipient_list = [email],
            #             fail_silently=False,
                        
            #         )
            return redirect('login')
    else:
        form = UserForm()  
    context = {'form':form}  

    return render(request, 'signup.html', context)

        
          
    
    
    

def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
                
                
			password = form.cleaned_data.get('password')
            
			user = authenticate(username=username, password=password)
            
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", context={"login_form":form})

def Logout(request):
    
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")
    
def ContactUs(request):
	if request.method == "POST": 
		name = request.POST.get('name')
		print(name)
		email = request.POST.get('email') 
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		if Contact.objects.filter(name=name, email=email):
			messages.warning(request,"email and name already exsist") 
			return redirect("contact")
		else:
			user = Contact(name=name,email=email,subject=subject,message=message)
			user.save()
			return redirect('login')
	return render(request,'contact.html')






	
def AddBlogPost(request):
	if request.user.is_authenticated:
        	
		categories = Category.objects.all()	
		
		
		if request.method == "POST" and request.FILES['image']:
			
			blog_title = request.POST.get('blog_title')
			print(blog_title)
			
			description = request.POST.get('description')
			print(description)
			image = request.FILES['image']
			name = request.POST.get('name')
			print(name)
			email = request.POST.get('email')
			print(email)
			categories1 = request.POST.get('categories')
			category1 = Category.objects.get(name_of_categories=categories1)
			
			user = AddPost(blog_title=blog_title,description=description,image=image,name=name,email=email,categories1_id=category1.id)
			
			user.save()
			
			return render(request,'post.html')
			

		return render(request,'post.html',{'categories':categories})
	else:
		return render(request,'login1.html')


def UpdateBlog(request , pk):
	addpost=AddPost.objects.get(id=pk)
	# return render(request,'edit.html',{'addpost':addpost})
	
	
	
	categories = Category.objects.all()	
	if request.method == "POST" and request.FILES['image']:
		blog_title = request.POST.get('blog_title')
		description = request.POST.get('description')
		image = request.FILES['image']
		name = request.POST.get('name')
		email = request.POST.get('email')
		print(email)
		categories1 = request.POST.get('categories')
		category1 = Category.objects.get(name_of_categories=categories1)
		# addpost=AddPost.objects.get(id=pk)
		addpost.blog_title=blog_title
		addpost.description=description
		addpost.image=image
		addpost.name=name
		addpost.email=email
		addpost.categories1_id=category1.id
		addpost.save()
		return render(request,'index.html')
			

	return render(request,'edit.html',{'categories':categories,'addpost':addpost})
	

	


def DeleteBlog(request,pk):
	addpost=AddPost.objects.get(id=pk)
	addpost.delete()
	return render(request,'index.html') 




def AddComment(request):
	addpost1 = AddPost.objects.all()
	if request.method == "POST" and request.FILES['image']:
		blog = request.POST.get('blog')
	
		comment = request.POST.get('Comment')
		image = request.FILES['image']
		name = request.POST.get('name')
		message = request.POST.get('message')
		addpost=AddPost.objects.get(id=blog)
		print(addpost.id)
		
		
		
	
		addcomment = Comment(comment=comment,image=image,name=name,message=message)
			
		addcomment.save()
		return render(request,'comment.html')
			

	return render(request,'comment.html',{'addpost1':addpost1})




	
	
	
	
	
	