from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload, name='uploaddata'),
    path('notes/', views.allnotes, name='allnotes'),
    path('<int:id>/', views.update, name='updatedata'),
    path('delete/<int:id>/', views.delete, name='deletedata'),


]

