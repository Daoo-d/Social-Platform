from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile_page,name="profile_page"),
    path('<username>',views.profile_page,name="user_profile"),
    path('edit/',views.edit_profile,name="edit_profile_page"),
    path('delete/',views.delete_profile,name="del_profile")
]