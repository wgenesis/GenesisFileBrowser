from django.urls import path
from . import views

app_name='login'
#主路由
urlpatterns = [
    path('registerVaild',views.RegisterVaild),
    path('index/',views.Index),
    path('login/',views.Login),
    path('register/',views.Register),
    #path('register/',views.RegisterVaild),
    path('logout/',views.Logout),
]