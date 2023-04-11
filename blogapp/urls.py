from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # for displaying post detail
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),  # for adding new post
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
]
