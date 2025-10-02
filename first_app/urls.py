from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    # Index View (Trang chủ của app)
    path('', views.IndexView.as_view(), name='index'), 

    # === Team/Member CRUD Views ===
    path('about/', views.AboutView.as_view(), name='about'),
    path('add-member/', views.AddTeamMemberView.as_view(), name='add_member'),
    path('update-member/<int:pk>/', views.UpdateTeamMemberView.as_view(), name='update_member'),
    path('delete-member/<int:pk>/', views.DeleteTeamMemberView.as_view(), name='delete_member'),
    
    # === Post/Category Views ===
    path('category/', views.CategoryView.as_view(), name='category'),
    # View chi tiết bài viết (chấp nhận cả Comment POST)
    path('single-post/<int:pk>/', views.SinglePostView.as_view(), name='single-post'),

    # === Post CRUD Views ===
    # KHẮC PHỤC LỖI: Tên View đã được xác nhận khớp với views.py
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('update-post/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete-post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),

    # === Comment CRUD Views ===
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),

    path('contact/', views.ContactView.as_view(), name='contact'), 
]
