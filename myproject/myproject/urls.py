"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),  # changed
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # changed
    path('delete_profile/<str:category>/<int:id>/', views.delete_profile, name='delete_profile'),  # changed
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # changed
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),  # changed

    path('bulk_unassign/', views.bulk_unassign_profiles, name='bulk_unassign_profiles'),

    path('forgot-password/', views.forgot_password, name='forgot_password'),

    
    path('mark-notification-read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),










] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
