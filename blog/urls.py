from django.urls import path
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
]
