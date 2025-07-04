from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
