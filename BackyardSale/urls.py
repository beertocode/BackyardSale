"""BackyardSale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.homeView.as_view(), name='home'),
                  path('dashboard/', include('DashBoard.urls', namespace='Dashboard')),
                  path('login/', views.loginUser, name='login'),
                  path('logout/', views.logoutUser, name='logout'),
                  path('register/', views.register, name='register'),
                  path('completedetails/',views.completeDetails,name='completedetails'),
                  path('updateuser/',views.updateuser,name='updateuser'),
                  path("items/<slug:slug>/<int:pk>", views.ItemView.as_view(), name='itemDetail'),
                  path('Subcategories/<slug:slug>/', views.subCategoryView.as_view(), name='subCatdetail'),
                  path('Categories/<slug:slug>/', views.CategoryView.as_view(), name='catDetail'),
                  path('search/', views.search , name='search'),
                  path('buy/<slug:slug>/<int:pk>',views.ItemBuy,name='itemBuy'),
                  path('auth/', include('social_django.urls', namespace='social')), #social network auth
                  path('requestItem/', views.createRequest.as_view(), name='requestItem'),
                  path('contactus/', views.contactus, name='contactus'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
