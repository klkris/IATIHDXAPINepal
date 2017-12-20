"""IATIHDXAPINepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from IATIHDXAPINepal import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('hxl/', views.HXLQuery.as_view()),
    path('updatehxl/', views.UpdateHXL.as_view()),
    path('iati/', views.IATIQuery.as_view()),
    path('updateiati/', views.UpdateIATI.as_view()),
    path('shelter/', views.ShelterQuery.as_view()),
    path('updateshelter/', views.UpdateShelter.as_view()),
    path('multitest/', views.MultiHXLandShelterView.as_view()),
    path('docs/', include_docs_urls(title='Documentation', public=False)),
]


urlpatterns = format_suffix_patterns(urlpatterns)

