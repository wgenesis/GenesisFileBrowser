from django.urls import path
from . import views

app_name='filebrowser'
#主路由
urlpatterns = [
    path('upload/',views.Upload),
    path('index/<str:username>',views.index,name='index'),
]