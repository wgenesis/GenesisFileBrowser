"""GenesisFileBrowser URL Configuration

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
import login.views as login_views
import filebrowser.views as filebrowser_views

urlpatterns = [
    path('registerVaild',login_views.RegisterVaild),
    path('admin/', admin.site.urls),
    path('index/',login_views.Index),
    path('login/',login_views.Login),
    path('register/',login_views.Register),
    path('upload/',filebrowser_views.Upload),
    path('member_index/',filebrowser_views.member_index,name='menber_index'),
    path('',login_views.Login),
    #path('register/',views.RegisterVaild),
    path('logout/',login_views.Logout),
]
