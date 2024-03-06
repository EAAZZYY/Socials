from django.urls import path
from . import views

app_name = 'grandiose'


urlpatterns = [
    path("",views.home,name='home'),
    path("post/",views.post,name="post"),
    path("like/",views.post_liked,name="like")
]