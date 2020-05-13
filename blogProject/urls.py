from django.contrib import admin
from django.urls import path
import blogapp.views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    path('blogMain/', blogapp.views.blogMain, name='blogMain'),
    path('blogMain/createBlog/', blogapp.views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blogMain/detail/<int:blog_id>/', blogapp.views.detail, name='detail'),
    path('blogMain/updateBlog/<int:blog_id>', blogapp.views.updateBlog, name='updateBlog'),
    path('blogMain/deleteBlog/<int:blog_id>', blogapp.views.deleteBlog, name='deleteBlog'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
