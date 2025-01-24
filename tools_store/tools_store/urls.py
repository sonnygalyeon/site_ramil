"""
URL configuration for tools_store project.

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from .views import logged_out, index
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('store/', views.store, name='store'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    # path('logout/', logged_out, name='logout'),
    path('about/', views.about_view, name='about'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('contact/', views.contact_view, name='contact'),
    path('forgot/', views.forgot_password_view, name='forgot'),

    # Django Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page=''), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)

