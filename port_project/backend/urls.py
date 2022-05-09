from django.urls import path
from backend import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'backend'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('view-blog/', views.view_blog, name='view_blog'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('delete_blog/<slug:slug>/', views.delete_post, name='delete_blog'),
    path('edit-blog/<slug:slug>/', views.edit_post, name='editpost'),
    path('view-blogpost/<slug:slug>/', views.view_post, name='view_blogpost'),
    path('change_password/', views.password_change, name='change_password'),
    path('logout_view-page/', views.signout, name='logout_view'),
    path('signin/',views.signin, name='signin'),
    
    
    
]