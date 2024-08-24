from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Tag
from .forms import CreatePost,EditPost
import requests
from bs4 import BeautifulSoup # type: ignore
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request,tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag=get_object_or_404(Tag,slug=tag)
    else:
        posts = Post.objects.all()
    Categories = Tag.objects.all()    
    return render(request,"a_posts/home.html",{
        "posts":posts,
        "tag":tag,
        "Categories":Categories
    })

def post_page(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,"a_posts/post_page.html",{
        "post":post
    })

@login_required
def create_post(request):
    form = CreatePost()
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            try:

                response = requests.get(form.data['url'])
                soup = BeautifulSoup(response.text,"html.parser")

                find_image=soup.select('meta[content^="https://live.staticflickr.com/"]')
                image = find_image[0]["content"]
                print(image)
                post.image = image

                find_title = soup.select('h1.photo-title ')
                title = find_title[0].text.strip()
                post.title= title

                find_artist = soup.select('a.owner-name')
                artist = find_artist[0].text.strip()
                post.artist =artist
                post.author = request.user
            except:
                messages.success(request,'data not found')
                return redirect('create_post')  

            post.save()
            form.save_m2m()
            messages.success(request,"New Post is added succesfully")
            return redirect("homepage")
    return render(request,"a_posts/create_post.html",{
        "form":form
    })

@login_required
def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk,author=request.user)
    if request.method=="POST":
        post.delete()
        messages.success(request,'Post deleted')
        return redirect('homepage')
    return render(request,"a_posts/delete_post.html",{
        "post":post
    })

@login_required
def edit_post(request,pk):
    post = get_object_or_404(Post,pk=pk,author=request.user)
    form=EditPost(instance=post)
    if request.method=='POST':
        form=EditPost(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post is updated successfully')
            return redirect('homepage')
    return render(request,"a_posts/edit_post.html",{
        "post":post,
        "form":form
    })    
