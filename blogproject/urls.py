"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from blogapp.views import all_blog,blog_detail,search,contact,post_by_filter

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',all_blog,name='all_blog'),
    path('post/<int:id>',blog_detail,name='blog_detail'),
    path('search/',search,name='search'),
    path('contact/',contact,name='contact'),
    path('post/filter/<int:id>',post_by_filter,name='post_by_filter'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)