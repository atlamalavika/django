
from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.Registration),
    path('login/',views.Login1),
    path('home/',views.Home),
    # path('logout/',views.Logout1),
    
]