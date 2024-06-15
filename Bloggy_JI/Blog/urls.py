from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # API TO Post a Comments
    path('BlogComment/', views.BlogComment, name='BlogComment'),
    path('VideoComment/', views.VideoComment, name='VideoComment'),
    path('ImageComment/', views.ImageComment, name='ImageComment'),
    path('BlogLike/<int:b_id>/', views.BlogLike, name='BlogLike'),
    path('VideoLike/<int:v_id>/', views.VideoLike, name='VideoLike'),
    path('ImageLike/<int:i_id>/', views.ImageLike, name='ImageLike'),
    path('DeleteBlog/<int:b_id>/', views.DeleteBlog, name='DeleteBlog'),
    path('DeleteVideo/<int:v_id>/', views.DeleteVideo, name='DeleteVideo'),
    path('DeleteImage/<int:i_id>/', views.DeleteImage, name='DeleteImage'),
    path('EditVideo/<int:v_id>/', views.EditVideo, name='EditVideo'),
    path('EditImage/<int:i_id>/', views.EditImage, name='EditImage'),
    path('EditBlog/<int:b_id>/', views.EditBlog, name='EditBlog'),
    path('EditBlog/<int:b_id>/', views.EditBlog, name='EditBlog'),
    # Templates
    path('', views.BlogHome, name='BlogHome'),
    path('Add_Blogs/<int:cat_id>/', views.Add_Blogs, name='Add_Blogs'),
    path('Video/', views.Video, name='Video'),
    path('FullSizeVideo/<int:v_id>/', views.FullSizeVideo, name='FullSizeVideo'),
    path('FullSizeImage/<int:i_id>/', views.FullSizeImage, name='FullSizeImage'),
    path('Add_Videos/', views.Add_Videos, name='Add_Videos'),
    path('Images/', views.Images, name='Images'),
    path('Add_Images/', views.Add_Images, name='Add_Images'),
    path('FindContent/', views.FindContent, name='FindContent'),
    path('ChatBot/', views.ChatBot, name='ChatBot'),
    path('Result/', views.Result, name='Result'),
    path('generate_content/', views.generate_content, name='generate_content'),
    path('BlogPosts/<int:b_id>', views.BlogPosts, name='BlogPosts'),
    path('Categories/<int:cat_id>', views.Categories, name='Categories'),
    path('Category_Search/', views.Category_Search, name='Category_Search'),
    path('Blog_Search/<int:cat_id>', views.Blog_Search, name='Blog_Search'),
    path('Video_Search/', views.Video_Search, name='Video_Search'),
    path('Image_Search/', views.Image_Search, name='Image_Search'),
    path('EditBlogForm/<int:b_id>/', views.EditBlogForm, name='EditBlogForm'),
    path('AddBlogForm/<int:cat_id>', views.AddBlogForm, name='AddBlogForm'),
    path('UserProfile/<int:id>', views.UserProfile, name='UserProfile'),

]
