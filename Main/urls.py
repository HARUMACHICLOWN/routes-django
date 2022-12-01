from django.urls import path
from RoutesApp import views

urlpatterns = [
    path('recent', views.recent),
    path('popular', views.most_popular),
    path('all', views.all_posts),
    path('post', views.post_comments_likes)
]