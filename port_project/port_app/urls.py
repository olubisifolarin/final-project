from unicodedata import name
from django.urls import path
from port_app import views
from django.conf import settings
from django.conf.urls.static import static
from port_app.views import Blog

app_name = 'port_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('blog-details/<slug:slug>/', views.blog_detail, name='detail_blog'),
    
    # path('blog-details/<slug:slug>/', views.blog_detail.as_view(model=Blog), name='detail_blog'),
   
]

