from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dash'),
    path('logout/', views.logout_user, name='logout')
]
