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
from django.urls import path
from blok.views import main_view , current_date_view , goodbye_view,product_view,category_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('current_date/',current_date_view),
    path('goodbye/',goodbye_view),
    path('product/',product_view, name='product'),
    path('category/', category_view, name='category')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
