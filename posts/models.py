from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500,null=True)
    artist = models.CharField(max_length=200,null=True)
    image = models.URLField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='posts')
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self) -> str:
        return f"{self.author}"    

class Tag(models.Model):
    name=models.CharField(max_length=20)
    image = models.FileField(upload_to="icons",null=True,blank=True)
    slug = models.SlugField(max_length=20,unique=True,null=False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['pk']

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="comments")
    parent_post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")        
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100,default=uuid.uuid4,primary_key=True,unique=True,null=False)

    def __str__(self) -> str:
        return f"{self.author.username} : {self.body[:30]}" 
    class Meta:
        ordering = ['-created']

class Reply(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="replies")
    parent_comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="replies")        
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100,default=uuid.uuid4,primary_key=True,unique=True,null=False)

    def __str__(self) -> str:
        return f"{self.author.username} : {self.body[:30]}" 
    class Meta:
        ordering = ['created']        