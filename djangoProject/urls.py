"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from blok.views import (main_view , current_date_view , goodbye_view,ProductView,category_view,create_product_view,
                        post_detail_view,category_product_view)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blok.urls')),
    path('auth/',include('user.urls')),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
