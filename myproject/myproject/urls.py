"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from community.views import *
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^list/', list, name='list'),
    re_path(r'^write/', write, name = 'write'),
    re_path(r'^view/(?P<num>[0-9]+)/$', view),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^write/', write, name='write'),
    # url(r'^list/', list, name='list'),
    # url(r'^view/(?P<num>[0-9]+)$', view),
]