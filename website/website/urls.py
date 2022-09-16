
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from predict import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^$',views.index,name="Homepage"),
    path('main/', views.AjaxHandler.as_view() ,name = 'main'),
    path('', views.home, name='home'),
]
