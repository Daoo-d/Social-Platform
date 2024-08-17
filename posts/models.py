from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500,null=True)
    artist = models.CharField(max_length=200,null=True)
    image = models.URLField(max_length=500)
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

class Tag(models.Model):
    name=models.CharField(max_length=20)
    image = models.FileField(upload_to="icons",null=True,blank=True)
    slug = models.SlugField(max_length=20,unique=True,null=False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['pk']