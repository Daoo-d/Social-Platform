from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile_page,name="profile_page"),
    path('edit/',views.edit_profile,name="edit_profile_page")
]