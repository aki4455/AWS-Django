"""
URL configuration for trydjango project.

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

from django.contrib import admin
from django.urls import include, path


from album.views import album_list, album_detail ,album_create,album_delete



urlpatterns = [
    #path('album/', include('album.urls')),

    path("admin/", admin.site.urls),

    
    
    path('album/', album_list, name='al-list'),
    path('album/create/', album_create, name='al-create'),
    path('album/<str:country>/', album_detail, name='al-detail'),
    path('album/<str:country>/delete/', album_delete, name='al-delete'),
    
    #path('album/<int:id>/delete/', album_delete, name='al-delete'),
    
    
]

