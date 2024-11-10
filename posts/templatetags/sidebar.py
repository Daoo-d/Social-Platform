from django.template import Library
from ..models import Tag,Post
from django.db.models import Count

register = Library()

@register.inclusion_tag("include/sidebar.html")
def sidebar_view(tag=None,user = None):
    Categories = Tag.objects.all()
    top_posts = Post.objects.annotate(num_likes = Count('likes')).filter(num_likes__gt=0).order_by("-num_likes")
    context = {
        "Categories":Categories,
        "tag":tag,
        "top_posts":top_posts,
        "user":user
    }
    return context