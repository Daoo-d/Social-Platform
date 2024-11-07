from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('category/<tag>',views.home,name="category"),
    path('post/create',views.create_post,name="create_post"),
    path('post/delete/<int:pk>',views.delete_post,name="delete_post"),
    path('post/edit/<int:pk>',views.edit_post,name="edit_post"),
    path('post/<int:pk>',views.post_page,name="post_page"),
    path('commentsent/<int:pk>',views.comment_sent,name="comment_sent"),
    path('comment/delete/<id>',views.delete_comment,name="comment_delete"),
    path('replysent/<id>',views.reply_sent,name="reply_sent"),

]
