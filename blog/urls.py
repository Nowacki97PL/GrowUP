from django.urls import path

from blog.views import PostsListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path('posty/', PostsListView.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
